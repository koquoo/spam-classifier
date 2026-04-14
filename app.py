import streamlit as st
import joblib

# 1. Load the trained brain you downloaded from Colab
# Make sure the filename matches exactly!
model = joblib.load('spam_model (2).pkl')

# 2. LOVELY UI - Custom CSS for the "Cute" vibe
st.set_page_config(page_title="SpamGuard 🌸", page_icon="💌")

st.markdown("""
    <style>
    .main {
        background-color: #fff5f8;
    }
    h1 {
        color: #ff8fa3;
        font-family: 'Arial';
        text-align: center;
    }
    .stTextArea textarea {
        border: 2px solid #ffb3c1;
        border-radius: 20px;
    }
    .stButton>button {
        background-color: #ffb3c1;
        color: white;
        border-radius: 25px;
        height: 3em;
        width: 100%;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #ff8fa3;
        color: white;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. THE APP CONTENT
st.title("💌 Spam Email Classifier")
st.write("---")
st.write("Paste the message below and let the AI do its magic! ✨")

email_input = st.text_area("Message to analyze:", placeholder="e.g., Congratulations! You've won a $1000 gift card!", height=200)

if st.button("Scan for Spam 🎀"):
    if email_input:
        # Predict using the model
        prediction = model.predict([email_input])
        
        # Display the result with some flair
        if prediction[0] == 'spam' or prediction[0] == 1:
            st.error("🚨 **RESULT: SPAM**")
            st.write("This looks like a suspicious pattern. Be careful! 🍬")
        else:
            st.success("🌸 **RESULT: SAFE**")
            st.write("This message seems totally fine. You're good to go!")
    else:
        st.warning("Please enter some text first, bestie! 💕")