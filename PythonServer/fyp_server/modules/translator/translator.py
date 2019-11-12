from googletrans import Translator  # Import Translator module from googletrans package
import re

translator = Translator(service_urls=[
'translate.google.com',
'translate.google.co.kr',
])

# Create object of Translator.
def translate(src_list, src_lang, dest_lang):
    translated = []
    translations = translator.translate(src_list, src=src_lang, dest=dest_lang)
    for translation in translations:
        translated.append(translation.text)
    return 200, translated

