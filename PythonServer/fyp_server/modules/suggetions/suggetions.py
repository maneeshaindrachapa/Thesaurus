f = open("modules/suggetions/suggetions_data.txt",'r', encoding='utf-8')
data = f.readlines()
data = [s[:-1].lower() for s in data]

def suggest(word,wordCount):
    return [s for s in data if (s.startswith(word.lower()))][:wordCount]