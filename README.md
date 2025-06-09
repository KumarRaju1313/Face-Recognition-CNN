# 🧠 Face Re-Identification Using Deep Learning

This project aims to build a **Face Re-Identification System** capable of recognizing individuals based on facial images. It uses three state-of-the-art deep learning models: **MobileNetV2**, **VGG16**, and **ResNet50V2**, trained on a custom dataset of 7 individuals.

---

## 📌 Project Objective

The goal is to identify a person from a face image, even if the image has been altered through augmentations like blurring, flipping, or converting to grayscale. This is useful in surveillance, access control, or verification systems.

---

## 🧾 Dataset Information

- **Classes (Individuals):**
  1. Chakri  
  2. Sai Priya  
  3. Uday  
  4. Vijay  
  5. Kavya Sri  
  6. Gowthami  
  7. Kumar

- **Number of Images:**
  - 4000 images per class (after augmentation)
  - **Total Images:** 31,976
  - **Split Ratio:** 80% Training | 10% Validation | 10% Testing

- **Augmentations Applied:**
  - Gaussian Blur
  - Grayscale Conversion
  - Horizontal Flipping

---

## 🧠 Models Used

| Model        | Description |
|--------------|-------------|
| **MobileNetV2** | Lightweight and efficient; ideal for mobile deployment |
| **VGG16**        | Deep and widely used for image classification tasks |
| **ResNet50V2**   | Deep residual learning with skip connections |

---

## ⚙️ Training Configuration

- **Batch Size:** 32  
- **Epochs:** 10 *(with early stopping)*  
- **Optimizer:** Adam  
- **Loss Function:** Categorical Crossentropy  
- **Early Stopping:** Enabled, with best model checkpointing

### 📉 Best Epochs & Validation Loss

| Model         | Best Epoch | Validation Loss |
|---------------|------------|-----------------|
| MobileNetV2   | 3          | 1.53            |
| ResNet50V2    | 3          | 0.051           |
| VGG16         | 2          | 0.19            |

---

## 🚀 Speed Comparison

### 🔧 Keras (.h5 models)

| Model        | Size    | 10 Images | 50 Images | 100 Images |
|--------------|---------|-----------|-----------|------------|
| MobileNetV2  | 146 MB  | 18.75 s   | 58.72 s   | 117.18 s   |
| VGG16        | 216 MB  | 5.11 s    | 19.62 s   | 39.62 s    |
| ResNet50V2   | 282 MB  | 11.01 s   | 12.85 s   | 25.78 s    |

### 🪄 ONNX (.onnx models)

| Model        | Size     | 10 Images | 50 Images | 100 Images |
|--------------|----------|-----------|-----------|------------|
| MobileNetV2  | 48.4 MB  | 0.27 s    | 1.23 s    | 1.73 s     |
| VGG16        | 72.1 MB  | 1.98 s    | 9.14 s    | 18.18 s    |
| ResNet50V2   | 153 MB   | 0.83 s    | 3.18 s    | 6.21 s     |

---

## 🧪 Sample Predictions

### ✅ MobileNetV2 Predictions (Examples)

| Predicted Class | Actual Class |
|------------------|---------------|
| Uday             | Chakri        |
| Chakri           | Chakri        |
| Gowthami         | Gowthami      |
| Uday             | Kavya         |

### ✅ VGG16 Predictions (Examples)

| Predicted Class | Actual Class |
|------------------|---------------|
| Chakri           | Chakri        |
| Gowthami         | Gowthami      |
| Kavya            | Kavya         |

### ✅ ResNet50V2 Predictions (Examples)

| Predicted Class | Actual Class |
|------------------|---------------|
| Chakri           | Chakri        |
| Gowthami         | Gowthami      |
| Kavya            | Kavya         |

---

