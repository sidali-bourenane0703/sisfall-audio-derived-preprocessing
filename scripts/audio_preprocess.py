import os, random
import numpy as np
import librosa

from audiomentations import Compose, AddGaussianNoise, TimeStretch, PitchShift

# Reproducibility
random.seed(1337)
np.random.seed(1337)

augmentations = Compose([
    AddGaussianNoise(min_amplitude=0.001, max_amplitude=0.015, p=0.5),
    TimeStretch(min_rate=0.8, max_rate=1.2, p=0.5),
    PitchShift(min_semitones=-4, max_semitones=4, p=0.5)
])

def extract_centered_window(x, sr, dur_sec=3.0):
    target = int(dur_sec * sr)
    if len(x) <= target:
        return np.pad(x, (0, target - len(x)))
    hop = int(0.05 * sr)  # 50 ms hop
    best_i, best_e = 0, -1
    for i in range(0, len(x)-target+1, hop):
        e = np.sum(x[i:i+target]**2)
        if e > best_e:
            best_e, best_i = e, i
    return x[best_i:best_i+target]

def extract_audio_features(audio_path, target_duration=3.0, augment=False,
                           n_mels=128, n_fft=2048, hop_length=512):
    y, sr = librosa.load(audio_path, sr=None, mono=True)

    peak = np.max(np.abs(y))
    if peak > 0:
        y = y / peak

    # center on most-energetic 3 s (to “focus on fall noise” as described)
    y = extract_centered_window(y, sr, dur_sec=target_duration)

    if augment:
        y = augmentations(samples=y, sample_rate=sr)

    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels,
                                       n_fft=n_fft, hop_length=hop_length, power=2.0)
    S_db = librosa.power_to_db(S, ref=np.max)

    # If your CNN expects 3 channels, keep this; otherwise return S_db[..., None]
    S_rgb = np.repeat(S_db[..., None], 3, axis=-1)
    return S_rgb
 



X_train_features = [extract_audio_features(fp, augment=True)  for fp in all_audio_files_train]
X_test_features  = [extract_audio_features(fp, augment=False) for fp in all_audio_files_test]
                          
