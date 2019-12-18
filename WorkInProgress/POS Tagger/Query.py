import requests
import json
import sys
f = open(sys.argv[1])
f2 = open(sys.argv[2], 'w')

counter = 0
for line in f:

    line = line.strip()
    words = line.split()
    final_word = words[-1]
    if final_word.endswith('.'):
        words[-1] = final_word[:-1]
        words.append('.')

    line = " ".join(words)
    counter += 1
    r = requests.post("http://192.248.8.241:8080/api/v1/pos/sinhala",
                      data={'sentence': line})
    try:
        for data in r.json()['data']:
            print("%s %s" % (data['token'], data['tag'][0]), file=f2)
        print("", file=f2)
        print(counter)
    except:
        print(line)
        print("error")

