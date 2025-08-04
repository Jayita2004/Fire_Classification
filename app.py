import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("Best_fire_detection_model.pkl")
scaler = joblib.load("scaler.pkl")

# --- Custom CSS for professional fire-themed UI ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #1a1a1a, #3b0a0a);
        font-family: 'Segoe UI', sans-serif;
    }

    .main {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 0px 20px #ff4e00;
        color: white;
    }

    .stButton>button {
        background-color: #ff4e00;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        box-shadow: 0 0 10px #ff4e00;
    }

    .stButton>button:hover {
        background-color: #ff2200;
        box-shadow: 0 0 20px #ff2200;
    }

    .fire-icon {
        font-size: 3rem;
        text-align: center;
        color: #ffcc00;
        animation: flicker 1s infinite;
    }

    @keyframes flicker {
        0% {opacity: 1;}
        50% {opacity: 0.6;}
        100% {opacity: 1;}
    }

    .fire-title {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        text-shadow: 0 0 10px #ff6e40;
        margin-bottom: 10px;
    }

    .centered-text {
        text-align: center;
        font-size: 1rem;
        color: #cccccc;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Fire icons and title
st.markdown('<div class="fire-icon">🔥 🔥 🔥</div>', unsafe_allow_html=True)
st.markdown('<div class="fire-title">Fire Type Classification</div>', unsafe_allow_html=True)
st.markdown('<div class="centered-text">Predict fire type from MODIS satellite data</div>', unsafe_allow_html=True)

with st.container():
    with st.form(key='fire_form'):
        brightness = st.number_input("Brightness", value=300.0)
        bright_t31 = st.number_input("Brightness T31", value=290.0)
        frp = st.number_input("Fire Radiative Power (FRP)", value=15.0)
        scan = st.number_input("Scan", value=1.0)
        track = st.number_input("Track", value=1.0)
        confidence = st.selectbox("Confidence Level", ["low", "nominal", "high"])

        # Map confidence
        confidence_map = {"low": 0, "nominal": 1, "high": 2}
        confidence_val = confidence_map[confidence]

        submit = st.form_submit_button("🔍 Predict Fire Type")

        if submit:
            input_data = np.array([[brightness, bright_t31, frp, scan, track, confidence_val]])
            scaled_input = scaler.transform(input_data)
            prediction = model.predict(scaled_input)[0]

            fire_types = {
                0: "Vegetation Fire",
                2: "Other Static Land Source",
                3: "Offshore Fire"
            }

            result = fire_types.get(prediction, "❓ Unknown")
            st.success(f"**Predicted Fire Type:** {result}")
