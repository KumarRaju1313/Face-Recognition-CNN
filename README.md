# 🧠 Face Re-Identification Using Deep Learning

This project implements a **Face Re-Identification System** to recognize individuals based on facial features using deep learning. Three state-of-the-art CNN models were trained and compared for accuracy, speed, and deployment readiness.

---

## 📌 Project Objective

To classify faces of known individuals—even when the images are altered via augmentation—using MobileNetV2, VGG16, and ResNet50V2. This system can be extended to surveillance, biometric verification, or access control.

---

## 🧾 Dataset Information

- **Total Individuals (Classes):**
  1. Chakri  
  2. Sai Priya  
  3. Uday  
  4. Vijay  
  5. Kavya Sri  
  6. Gowthami  
  7. Kumar

- **Total Images:** 31,976  
- **Images per Class (after augmentation):** ~4000  
- **Train/Val/Test Split:** 80% / 10% / 10%

### 📈 Augmentations Applied

- Gaussian Blur  
- Grayscale Conversion  
- Horizontal Flip  

---

## 🧠 Models Used

| Model        | Description |
|--------------|-------------|
| **MobileNetV2** | Lightweight, mobile-friendly CNN |
| **VGG16**        | Classic deep CNN for image classification |
| **ResNet50V2**   | Residual network with skip connections |

---

## ⚙️ Training Configuration

- **Batch Size:** 32  
- **Epochs:** 10 (Early Stopping enabled)  
- **Optimizer:** Adam  
- **Loss Function:** Categorical Crossentropy  

### 📉 Best Epochs & Validation Loss

| Model         | Best Epoch | Validation Loss |
|---------------|------------|-----------------|
| MobileNetV2   | 3          | 1.53            |
| ResNet50V2    | 3          | 0.051           |
| VGG16         | 2          | 0.19            |

---

## 🚀 Inference Speed Comparison

### 🔧 Keras (.h5 format)

| Model        | Size    | 10 Images | 50 Images | 100 Images |
|--------------|---------|-----------|-----------|------------|
| MobileNetV2  | 146 MB  | 18.75 s   | 58.72 s   | 117.18 s   |
| VGG16        | 216 MB  | 5.11 s    | 19.62 s   | 39.62 s    |
| ResNet50V2   | 282 MB  | 11.01 s   | 12.85 s   | 25.78 s    |

### 🪄 ONNX (.onnx format)

| Model        | Size     | 10 Images | 50 Images | 100 Images |
|--------------|----------|-----------|-----------|------------|
| MobileNetV2  | 48.4 MB  | 0.27 s    | 1.23 s    | 1.73 s     |
| VGG16        | 72.1 MB  | 1.98 s    | 9.14 s    | 18.18 s    |
| ResNet50V2   | 153 MB   | 0.83 s    | 3.18 s    | 6.21 s     |

---

## 🧪 Sample Predictions

### ✅ MobileNetV2

| Predicted Class | Actual Class |
|------------------|---------------|
| Uday             | Chakri        |
| Chakri           | Chakri        |
| Gowthami         | Gowthami      |
| Uday             | Kavya         |

### ✅ VGG16

| Predicted Class | Actual Class |
|------------------|---------------|
| Chakri           | Chakri        |
| Gowthami         | Gowthami      |
| Kavya            | Kavya         |

### ✅ ResNet50V2

| Predicted Class | Actual Class |
|------------------|---------------|
| Chakri           | Chakri        |
| Gowthami         | Gowthami      |
| Kavya            | Kavya         |

---

## ✅ Summary

- **Best Overall Accuracy:** ResNet50V2  
- **Fastest Inference (ONNX):** MobileNetV2  
- **Best for Mobile Deployment:** MobileNetV2  
- **Most Accurate:** ResNet50V2 (low validation loss)

This project demonstrates how model choice, deployment format, and preprocessing affect performance in face re-identification tasks.

---

## 📦 Requirements

Install dependencies using:

```bash
pip install numpy pandas opencv-python tensorflow keras scikit-learn matplotlib onnx onnxruntime
