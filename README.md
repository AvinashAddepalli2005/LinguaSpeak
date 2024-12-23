# README for LinguaSpeak

**LinguaSpeak** is a Python-based voice-to-voice translator that allows users to seamlessly recognize speech, detect the spoken language, translate it into a desired target language, and generate audio output for the translated text. It is ideal for breaking language barriers and enabling smooth communication across different languages.

---

## Features
- **Speech Recognition**: Captures and recognizes spoken words using Google Speech Recognition.
- **Language Detection**: Automatically detects the language of the recognized speech using `langdetect`.
- **Translation**: Translates the detected language to the user-specified target language using `deep-translator`.
- **Audio Generation**: Converts the translated text into an audio file using Google Text-to-Speech (gTTS).
- **Multi-language Support**: Supports a range of Indian languages like Hindi, Telugu, Tamil, Kannada, Malayalam, and Bengali.

---

## Prerequisites
Before running the program, ensure the following Python libraries are installed:
- `speechrecognition`
- `deep-translator`
- `langdetect`
- `gTTS`

You can install these libraries using pip:
```bash
pip install speechrecognition deep-translator langdetect gtts
```

---

## Usage Instructions

1. **Run the Program**:
   Execute the script in your Python environment.

2. **Input Target Language**:
   When prompted, enter the target language name (e.g., `Hindi`, `Telugu`, etc.).

3. **Speak into the Microphone**:
   Wait for the "Listening..." prompt and speak clearly into your microphone.

4. **Output**:
   - Recognized text will be displayed.
   - Detected language will be printed.
   - Translated text will be shown in the terminal.
   - An audio file of the translated text will be saved in the `outputs` folder and played automatically.

---

## Example Run
- **Input**: Speak in English, "Hello, how are you?"
- **Target Language**: Hindi
- **Output**:
  - Recognized Text: "Hello, how are you?"
  - Detected Language: `en` (English)
  - Translated Text in Hindi: "नमस्ते, आप कैसे हैं?"
  - Audio File: `outputs/captured_voice_Hindi.mp3`

---

## Supported Languages
- Hindi (`hi`)
- Telugu (`te`)
- Kannada (`kn`)
- Tamil (`ta`)
- Malayalam (`ml`)
- Bengali (`bn`)

---

## Notes
- Ensure your microphone is connected and functional before running the program.
- For best results, speak clearly in a quiet environment.
- The program currently supports a predefined set of languages. You can extend the `language_map` dictionary to add more.

---

## License
This project is open-source and free to use. Contributions and improvements are welcome!

---

Enjoy breaking language barriers with **LinguaSpeak**!
