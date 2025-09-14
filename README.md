# SisFall Audio Preprocessing and Augmentation

This repository provides scripts and derived data for **audio preprocessing and augmentation** from the [Sucerquia, A., López, J.D., Vargas-Bonilla, J.F.: SisFall: A fall and movement dataset. Sensors. 17, 198 (2017)).  
It enables reproducible pipelines for generating mel-spectrogram features used in our paper:

**"Audio-Visual Multimodal Fall Detection to Ensure the Safety of Elderly People in Intelligent Buildings: An Innovative Approach Using LSTM, CNN, and a Shallow Neural Network"**  
Sid Ali Bourenane · Sid Ahmed Henni · 2025

---

## 📂 Contents
- `scripts/audio_preprocess.py` — preprocessing and augmentation script.  
- `requirements.txt` — Python dependencies.  
- `audio dataset.zip` — example processed dataset (derived, not raw SisFall).  

---

## ⚙️ Features
- Trim fall samples to ~3s duration.  
- Normalize audio amplitude.  
- Apply augmentations:
  - Gaussian Noise
  - Time Stretch
  - Pitch Shift  
- Generate mel-spectrograms (`128x128x1` normalized).  

---

## 🚀 Usage
Install dependencies:
```bash
pip install -r requirements.txt

