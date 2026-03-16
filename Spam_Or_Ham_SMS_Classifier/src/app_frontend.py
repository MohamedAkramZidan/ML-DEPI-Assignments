import streamlit as st
import requests

# Streamlit page config
st.set_page_config(page_title="Spam Detector", page_icon="✉️")

st.title("Spam Detector")
st.write("Enter a text message and the model will predict whether it's spam or not.")

# User input
user_input = st.text_area("Enter your text here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        try:
            # Call FastAPI endpoint
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={"text": user_input}
            )
            if response.status_code == 200:
                prediction = response.json()["prediction"]
                if prediction == 1:
                    st.error("⚠️ This is likely SPAM!")
                else:
                    st.success("✅ This is NOT spam.")
            else:
                st.error(f"Error from API: {response.status_code}")
        except Exception as e:
            st.error(f"Failed to reach API: {e}")