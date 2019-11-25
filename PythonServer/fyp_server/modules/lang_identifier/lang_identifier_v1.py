def predict_lang(word):
    if len(word) > 0:
        try:
            si_count = 0
            en_count = 0
            other_count = 0

            for char in word:
                ord_val = ord(char)
                if (65 <= ord_val <= 90) or (97 <= ord_val <= 122):
                    en_count += 1
                elif 3456 <= ord_val <= 3583:
                    si_count += 1
                else:
                    other_count += 1

            si_presen = si_count / len(word)
            en_presen = en_count / len(word)
            other_presen = other_count / len(word)

            lang_dict = {'si': si_presen, 'en': en_presen, 'other': other_presen}

            return 200, max(lang_dict, key=lang_dict.get)
        except ZeroDivisionError:
            return 404, "No input word"
    else:
        return 404, "No input word"
