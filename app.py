import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps

# Set up app config
st.set_page_config(page_title="Fire Detection from Satellite", layout="centered")

st.title("Fire Detection from Satellite Images")
st.write("Upload a satellite image to detect presence of Fire or Not Fire")

# Load model (cache it)
@st.cache_resource
def load_fire_model():
    model = load_model("fire_detection_model.h5")
    return model

model = load_fire_model()

# Class labels (you can update this to match your training config)
class_names = ["No Fire", "Fire 🔥"]

# Upload image section
uploaded_file = st.file_uploader("📷 Upload Satellite Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocessing (based on how your model was trained!)
    input_shape = (64, 64)  # Update if your model uses different shape

    image_resized = image.resize(input_shape)
    img_array = np.array(image_resized) / 255.0
    img_array = img_array.reshape(1, *input_shape, 3)

    if st.button("🧠 Detect Fire"):
        with st.spinner("Analyzing image..."):
            prediction = model.predict(img_array)
            predicted_class = np.argmax(prediction)
            confidence = float(prediction[0][predicted_class]) * 100

            if confidence < 0.01:
                confidence_display = "< 0.01%"
            else:
                confidence_display = f"{confidence:.2f}%"

            st.subheader("Result:")
            st.success(f"Prediction: *{class_names[predicted_class]}*")
            st.info(f"Confidence: *{confidence_display}*")
