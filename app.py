import streamlit as st
import requests
from gtts import gTTS
import io

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Language Translator")
st.write("Translate your text into different languages.")

languages = {
    "English": "en",
    "Urdu": "ur",
    "Arabic": "ar",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Hindi": "hi",
    "Chinese": "zh-CN",
    "Italian": "it",
    "Turkish": "tr"
}

source = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

target = st.selectbox(
    "Select Target Language",
    list(languages.keys()),
    index=1
)

user_text = st.text_area(
    "Enter Text",
    placeholder="Write something to translate..."
)

if st.button("Translate"):
    if not user_text.strip():
        st.warning("Please enter some text.")

    elif source == target:
        st.warning("Please select different languages.")

    else:
        try:
            with st.spinner("Translating..."):

                url = "https://api.mymemory.translated.net/get"

                params = {
                    "q": user_text,
                    "langpair": f"{languages[source]}|{languages[target]}"
                }

                response = requests.get(
                    url,
                    params=params,
                    timeout=30
                )

                response.raise_for_status()
                data = response.json()

                if data.get("responseStatus") == 200:
                    translated_text = data["responseData"]["translatedText"]

                    st.session_state["translation"] = translated_text
                    st.session_state["target_code"] = languages[target]

                else:
                    st.error("Translation failed. Please try again.")

        except requests.RequestException as e:
            st.error(f"API Error: {e}")

if "translation" in st.session_state:

    st.subheader("Translated Text")

    translated_text = st.session_state["translation"]

    st.text_area(
        "Translation Result",
        value=translated_text,
        height=120,
        disabled=True
    )

    # Copy Button
    st.code(translated_text, language=None)
    st.caption("Use the copy icon on the code block to copy the translation.")

    # Text to Speech
    if st.button("🔊 Listen to Translation"):
        try:
            audio = io.BytesIO()

            speech = gTTS(
                text=translated_text,
                lang=st.session_state["target_code"]
            )

            speech.write_to_fp(audio)
            audio.seek(0)

            st.audio(audio, format="audio/mp3")

        except Exception as e:
            st.error(f"Audio Error: {e}")

st.divider()
st.caption("Language Translator Tool | AI Internship Project")