import streamlit as st
import onnxruntime as ort
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import time

models = {
    "ResNet50V2 (ONNX)": r"C:\Users\Lenovo\Desktop\Face_identification\Main_data\Model_resnet50v2.onnx",
    "VGG16 (ONNX)": r"C:\Users\Lenovo\Desktop\Face_identification\Main_data\Model_vgg16.onnx",
    "MobileNet (ONNX)": r"C:\Users\Lenovo\Desktop\Face_identification\Main_data\Model_mobilenet.onnx"
}

class_labels = ['chakri','gowthami','kavya','kumar','sai','uday','vijay']

st.title("🎭 Face ReIdentification App")
st.sidebar.title("🔧 Model Selection")
selected_model = st.sidebar.selectbox("Select a Model (ONNX)", list(models.keys()))
onnx_model_path = models[selected_model]
session = ort.InferenceSession(onnx_model_path)

input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

uploaded_files = st.file_uploader("📷 Upload images (you can select multiple)", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    st.write("Processing images...")

    predictions = []
    batch_start_time = time.time()

    for uploaded_file in uploaded_files:
        img = Image.open(uploaded_file).resize((256, 256))  
        input_tensor = image.img_to_array(img)
        input_tensor = np.expand_dims(input_tensor, axis=0).astype(np.float32)
        start_time = time.time()
        output = session.run([output_name], {input_name: input_tensor})[0]
        end_time = time.time()
        probabilities = np.exp(output) / np.sum(np.exp(output), axis=1, keepdims=True)
        predicted_class_index = np.argmax(probabilities)
        predicted_class = class_labels[predicted_class_index]

        predictions.append((uploaded_file.name, predicted_class, img, end_time - start_time))

    batch_end_time = time.time()
    total_batch_time = batch_end_time - batch_start_time

    st.write("### 📝 Predictions:")
    for img_name, predicted_class, img, prediction_time in predictions:
        col1, col2 = st.columns([1, 3])  
        with col1:
            st.image(img, caption=img_name, use_column_width=False) 
        with col2:
            st.write(f"**Predicted Class:** {predicted_class} - Time: {prediction_time:.6f} seconds")
        st.markdown("---") 

    st.write(f"\n**Total Time for Processing Batch:** {total_batch_time:.6f} seconds")
