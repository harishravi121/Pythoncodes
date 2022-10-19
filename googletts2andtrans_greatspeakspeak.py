from google_speech import Speech
from googletrans import Translator

sent='''भारतीय टीम के पूर्व कप्तान विराट कोहली ने टी20 वर्ल्ड कप 2022 के लिए अपनी कमर कस ली है. इसकी तैयारी के लिए कोहली ने जिम में भी जमकर पसीना बहाना शुरू क'''
srclang='hi'
destlang='en'
translator = Translator()
translated = translator.translate(sent, src=srclang, dest=destlang)
speech = Speech(sent, srclang)
speech.play()
speech = Speech(translated.text, destlang)
speech.play()

