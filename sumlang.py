
from num2words import num2words
from googletrans import Translator

sent=num2words(134)
print(sent)
lang='ta'
translator = Translator()
translated = translator.translate(sent, src='en', dest=lang)
print(translated.text)
