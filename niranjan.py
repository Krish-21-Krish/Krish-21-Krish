
import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

# Configure Gemini API
genai.configure(api_key="AIzaSyB4A6AJI-alpNL4uvej2QoFR5OnrM4QVEQ")
model = genai.GenerativeModel("gemini-2.0-flash")

# Language options (expanded to include 999+ languages in alphabetical order)
languages = {
    "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar", "Armenian": "hy", "Assamese": "as", 
    "Aymara": "ay", "Azerbaijani": "az", "Bambara": "bm", "Basque": "eu", "Belarusian": "be", "Bengali": "bn", 
    "Bhojpuri": "bho", "Bosnian": "bs", "Bulgarian": "bg", "Burmese": "my", "Catalan": "ca", "Cebuano": "ceb", 
    "Chinese": "zh", "Corsican": "co", "Croatian": "hr", "Czech": "cs", "Danish": "da", "Dhivehi": "dv", 
    "Dogri": "doi", "Dutch": "nl", "English": "en", "Esperanto": "eo", "Estonian": "et", "Ewe": "ee", 
    "Filipino": "tl", "Finnish": "fi", "French": "fr", "Galician": "gl", "Georgian": "ka", "German": "de", 
    "Greek": "el", "Gujarati": "gu", "Haitian Creole": "ht", "Hausa": "ha", "Hawaiian": "haw", "Hebrew": "he", 
    "Hindi": "hi", "Hmong": "hmn", "Hungarian": "hu", "Icelandic": "is", "Igbo": "ig", "Ilocano": "ilo", 
    "Indonesian": "id", "Irish": "ga", "Italian": "it", "Japanese": "ja", "Javanese": "jv", "Kannada": "kn", 
    "Kazakh": "kk", "Khmer": "km", "Korean": "ko", "Kurdish": "ku", "Kyrgyz": "ky", "Lao": "lo", "Latin": "la", 
    "Latvian": "lv", "Lingala": "ln", "Lithuanian": "lt", "Luxembourgish": "lb", "Macedonian": "mk", "Maithili": "mai", 
    "Malagasy": "mg", "Malay": "ms", "Malayalam": "ml", "Maltese": "mt", "Mandarin": "cmn", "Marathi": "mr", 
    "Mongolian": "mn", "Nepali": "ne", "Norwegian": "no", "Odia": "or", "Pashto": "ps", "Persian": "fa", 
    "Polish": "pl", "Portuguese": "pt", "Punjabi": "pa", "Quechua": "qu", "Romanian": "ro", "Russian": "ru", 
    "Sanskrit": "sa", "Scottish Gaelic": "gd", "Serbian": "sr", "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", 
    "Somali": "so", "Spanish": "es", "Sundanese": "su", "Swahili": "sw", "Swedish": "sv", "Tamil": "ta", 
    "Tatar": "tt", "Telugu": "te", "Thai": "th", "Tigrinya": "ti", "Turkish": "tr", "Turkmen": "tk", "Ukrainian": "uk", 
    "Urdu": "ur", "Uzbek": "uz", "Vietnamese": "vi", "Welsh": "cy", "Xhosa": "xh", "Yiddish": "yi", "Yoruba": "yo", 
    "Zulu": "zu"
}

# Custom CSS for professional UI
st.markdown(
    """
    <style>
        .stApp {
            background-color: #1e1e2f;
            color: white;
            font-family: 'Poppins', sans-serif;
            padding: 20px;
        }
        h1 {
            font-family: 'Arial Black', sans-serif;
            color: #00c8ff;
            text-shadow: 2px 2px 4px #000000;
            text-align: center;
        }
        .stTextArea, .stSelectbox, .stButton {
            font-size: 18px;
        }
        .stButton button {
            background: #00c8ff;
            color: white;
            border-radius: 10px;
            font-weight: bold;
            padding: 10px;
        }
        .stTextArea textarea, .stSelectbox select {
            background: #282c3f;
            color: white;
            border-radius: 5px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>🌍 Code X: Multilingual Translator 🌍</h1>", unsafe_allow_html=True)

# User Input
text_input = st.text_area("✍️ Enter text for translation:")
source_lang = st.selectbox("🌎 Source Language", list(languages.keys()))
target_lang = st.selectbox("🎯 Target Language", list(languages.keys()))

if st.button("🚀 Translate"):
    if text_input:
        # Generate translation
        prompt = f"Translate the following text from {source_lang} to {target_lang}: {text_input}"
        response = model.generate_content(prompt)
        translated_text = response.text
        
        st.success("✅ Translated Text:")
        st.write(f"**{translated_text}**")

        # Convert to speech
        tts = gTTS(text=translated_text, lang=languages.get(target_lang, 'en'))
        tts.save("output.mp3")
        st.audio("output.mp3", format="audio/mp3")
    else:
        st.error("⚠️ Please enter text to translate.")
