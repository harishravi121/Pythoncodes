from google_speech import Speech
from googletrans import Translator

sent="I love you."
lang='hi'
translator = Translator()
translated = translator.translate(sent, src='en', dest=lang)

speech = Speech(translated.text, lang)

for i in range(1):
    speech.play()
