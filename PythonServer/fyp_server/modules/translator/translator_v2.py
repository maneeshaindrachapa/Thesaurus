from googletrans import Translator  # Import Translator module from googletrans package

translator = Translator(service_urls=[
'translate.google.com',
'translate.google.co.kr',
]) # Create object of Translator.

##translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog', 'good', 'video', 'well', 'public', 'books', 'high', 'school', 'years', 'privacy', 'items'],
##                                    dest='si')
##for translation in translations:
##    print(translation.origin, ' -> ', translation.text)
##

ab = translator.translate(['බල්ලා', 'නරියා', 'බකමූණා', 'පූසා'], dest='en')

for a in ab:
    print(a.text)

##words = ['The quick brown fox', 'jumps over', 'the lazy dog', 'good', 'video', 'well', 'public', 'books', 'high', 'school', 'years', 'privacy', 'items']
##
##def translate(src_list, src_lang, dest_lang):
##    translated = []
##    translations = translator.translate(src_list, src=src_lang, dest=dest_lang)
##    for translation in translations:
##        translated.append(translation.text)
##    return translated
##
##print (translate(words, 'en', 'si'))
    
    
