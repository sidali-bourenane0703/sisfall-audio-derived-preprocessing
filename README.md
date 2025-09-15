
# Audio Preprocessing and Augmentation for SisFall Audio Dataset

This repository provides **scripts and derived audio data** for preprocessing and augmentation from the dataset:  

> Sucerquia, A., López, J.D., Vargas-Bonilla, J.F. (2017). *SisFall: A fall and movement dataset.* Sensors, 17(1), 198. https://doi.org/10.3390/s17010198  

It enables **reproducible pipelines** for generating mel-spectrogram features used in our paper:

**"Audio-Visual Multimodal Fall Detection to Ensure the Safety of Elderly People in Intelligent Buildings: An Innovative Approach Using LSTM, CNN, and a Shallow Neural Network"**  
*Sid Ali Bourenane · Sid Ahmed Henni · 2025*

---

## Repository contents
- `audio dataset.zip` —  processed dataset (derived, not raw SisFall).
- `processed_audio/` – directory containing processed and augmented audio samples derived from SisFall.  
- `scripts/audio_preprocess.py` – Python script implementing preprocessing and augmentation pipeline.  
- `requirements.txt` – dependencies for reproducibility.  

---

## Preprocessing and Augmentation Pipeline

### 1. Audio Data Augmentation
To address the limited size of the SisFall dataset, we applied augmentation to increase both quantity and diversity of audio samples. The following techniques were applied to the original fall and non-fall audio files:

- **AddGaussianNoise**: amplitude range 0.001–0.015, probability 0.5  
- **TimeStretch**: rate 0.8–1.2, probability 0.5  
- **PitchShift**: shift −4 to +4 semitones, probability 0.5  

### 2. Audio Preprocessing
- **Trimming**: Each sample is trimmed to approximately 3 seconds, centering on the most energetic segment to capture the essential *fall* noise.  
- **Normalization**: Each sample is normalized by dividing by its maximum absolute value to ensure consistent amplitude.  
- **No additional preprocessing** (e.g., denoising) was applied.  

### 3. Feature Extraction
- From the preprocessed audio, **mel-spectrograms** are extracted (`n_mels=128` by default).  
- Features can be expanded to 3-channel (RGB-like) inputs for CNN compatibility.  

---

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>


---

## 🚀 Usage
Install dependencies:
```bash
pip install -r requirements.txt

