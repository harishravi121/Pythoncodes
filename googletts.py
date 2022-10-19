from google_speech import Speech

# say "Hello World"
text = "Hello World"
lang = "en"
speech = Speech(text, lang)


speech.play()
