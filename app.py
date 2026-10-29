
import streamlit as st
import joblib
import re

# Load the trained machine learning model
model = joblib.load("sms_cyber_threat_model.pkl")


st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📩",
    layout="centered"
)

st.title("📩 SMS Spam Detector")
st.write("A machine learning application to classify SMS messages as spam or ham.")

st.set_page_config(
    page_title="SMS CyberGuard",
    page_icon="🛡️"
)

message = st.text_area(
    "Enter an SMS message to analyse:",
    placeholder="Example: Congratulations! You won a prize. Click this link..."
)

def cybersecurity_checks(message):
    warnings = []
    text = message.lower()

    urgent_words = ["urgent", "immediately", "suspended", "blocked",
                    "verify your account", "act now"]
    sensitive_words = ["otp", "pin", "password", "cvv",
                       "bank details", "banking details"]
    prize_words = ["you won", "winner", "claim your prize",
                   "free gift", "cash prize"]

    if any(word in text for word in urgent_words):
        warnings.append("Uses urgent or threatening language.")

    if any(word in text for word in sensitive_words):
        warnings.append("Mentions sensitive information such as OTPs or passwords.")

    if any(word in text for word in prize_words):
        warnings.append("Contains a possible prize or reward scam indicator.")

    if re.search(r"https?://|www\.", text):
        warnings.append("Contains a web link. Check it carefully before opening.")

    return warnings

if st.button("Analyse Message"):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        prediction = model.predict([message])[0]
        warnings = cybersecurity_checks(message)

        st.subheader("Analysis Result")

        if str(prediction).lower() == "spam":
            st.error("🚨 ML Prediction: Spam")
        else:
            st.success("✅ ML Prediction: Not Spam (Ham)")

        if warnings:
            st.subheader("⚠️ Security Warnings")
            for warning in warnings:
                st.write("- " + warning)
        else:
            st.info("No warning indicators detected by the basic checks.")

        st.caption(
            "Prototype only: predictions can be wrong. "
            "Always verify suspicious messages independently."
        )
