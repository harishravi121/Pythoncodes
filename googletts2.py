from google_speech import Speech

# say "Hello World"
text = "நான் உன்னை நேசிக்கிறேன்d"
lang = "ta"
speech = Speech(text, lang)

for i in range(5):
    speech.play()
