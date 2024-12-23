import speech_recognition as spr
from deep_translator import GoogleTranslator
from gtts import gTTS
from langdetect import detect
import os

# Creating Recognizer() class object
recog1 = spr.Recognizer()
mc = spr.Microphone()

# Function to capture voice and recognize text
def recognize_speech(recog, source):
    try:
        recog.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        audio = recog.listen(source)
        recognized_text = recog.recognize_google(audio)
        return recognized_text
    except spr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return None
    except spr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Simulating frontend input for the target language
target_language_input = input("Enter the target language (e.g., 'Hindi', 'Telugu', 'Tamil'): ").strip()

# Mapping user input to language codes
language_map = {
    'Hindi': 'hi',
    'Telugu': 'te',
    'Kannada': 'kn',
    'Tamil': 'ta',
    'Malayalam': 'ml',
    'Bengali': 'bn'
}

if target_language_input not in language_map:
    print(f"Invalid language: {target_language_input}. Exiting.")
else:
    target_language_code = language_map[target_language_input]
    with mc as source:
        print("Speak now for language detection and translation...")
        MyText = recognize_speech(recog1, source)
    
    if MyText:
        print(f"Recognized Text: {MyText}")
        try:
            # Detect the language of the recognized sentence
            detected_language = detect(MyText)
            print(f"Detected Language: {detected_language}")
            
            # Translate the recognized sentence into the target language
            translator = GoogleTranslator(source=detected_language, target=target_language_code)
            translated_text = translator.translate(MyText)
            print(f"Translated Text in {target_language_input}: {translated_text}")
            
            # Generate audio for the translated text
            if not os.path.exists('outputs'):
                os.makedirs('outputs')
            audio_file = f"outputs/captured_voice_{target_language_input}.mp3"
            speak = gTTS(text=translated_text, lang=target_language_code, slow=False)
            speak.save(audio_file)
            os.system(f"start {audio_file}")  # For Windows; use 'open' for macOS and 'xdg-open' for Linux
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("No speech input detected. Exiting.")