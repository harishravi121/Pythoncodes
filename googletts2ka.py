from google_speech import Speech

# say "Hello World"
text = "ನಾನು ನಿನ್ನನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ"
lang = "kn"
speech = Speech(text, lang)

for i in range(5):
    speech.play()
