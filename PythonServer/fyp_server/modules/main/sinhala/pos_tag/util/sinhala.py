# This Python file uses the following encoding: utf-8
##
# (C) 2007, 2008, 2013, 2015, 2016 Muthiah Annamalai <ezhillang@gmail.com>
# (C) 2013 msathia <msathia@gmail.com>
##
# This file is dual licensed - originally GPL v3 from Ezhil, and
# then as part of open-tamil package in MIT license.
##
# Licensed under GPL Version 3

from sys import version
from copy import copy
import re
import operator

PYTHON3 = version > '3'
del version

if PYTHON3:
    import functools

 # 323


def to_unicode_repr(_letter):
    """ helpful in situations where browser/app may recognize Unicode encoding
        in the \u0b8e type syntax but not actual unicode glyph/code-point"""
    # Python 2-3 compatible
    return u"u'" + u"".join([u"\\u%04x" % ord(l) for l in _letter]) + u"'"


def letters_to_py(_letters):
    """ return list of letters e.g. uyir_letters as a Python list """
    return u"[u'" + u"',u'".join(_letters) + u"']"


# List of letters you can use
uyir_letters = [u"අ", u"ආ", u"ඇ", u"ඈ", u"ඉ",
                u"ඊ", u"උ", u"ඌ", u"x", u"x", u"x", u"x",
                u"එ", u"ඒ", u"ඓ", u"ඔ", u"ඕ", u"ඔෟ", u"අං", u"අඃ"]

ayudha_letter = u"ං"

mei_letters = [u"ක්", u"ඛ්", u"ග්", u"ඝ්",  u"ඩ්", u"ඟ්", u"ච්",
               u"ඡ්", u"ජ්", u"ඣ්", u"ඤ්", u"ට්", u"ඨ්",
               u"ඪ්", u"ණ්", u"ඬ්", u"ත්", u"ථ්", u"ද්",
               u"ධ්", u"න්", u"ඳ්", u"ප්", u"ඵ්", u"බ්", u"භ්",
               u"ම්", u"ඹ්", u"ය්", u"ර්", u"ල්", u"ව්", u"ශ්",
               u"ෂ්", u"ස්", u"හ්", u"ළ්", u"ෆ්"]


accent_symbols = [u"", u"ා", u"ැ", u"ෑ", u"ි", u"ී", u"ු", u"ූ",
                  u"ෘ", u"ෘෘ", u"ෟ", u"ෟෟ", u"ෙ", u"ේ", u"ෛ", u"ො", u"ෝ", u"ෞ"]


pulli_symbols = [u"්"]
agaram_letters = [u"ක", u"ඛ", u"ග", u"ඝ", u"ඩ", u"ඟ", u"ච",
                  u"ඡ", u"ජ", u"ඣ", u"ඤ", u"ට", u"ඨ",
                  u"ඪ", u"ණ", u"ඬ", u"ත", u"ථ", u"ද",
                  u"ධ", u"න", u"ඳ", u"ප", u"ඵ", u"බ", u"භ",
                  u"ම", u"ඹ", u"ය", u"ර", u"ල", u"ව", u"ශ",
                  u"ෂ", u"ස", u"හ", u"ළ", u"ෆ"]

sanskrit_letters = [u"ஶ", u"ஜ", u"ஷ", u"ஸ", u"ஹ", u"க்ஷ"]
sanskrit_mei_letters = [u"ஶ்", u"ஜ்", u"ஷ்", u"ஸ்", u"ஹ்", u"க்ஷ்"]

grantha_mei_letters = copy(mei_letters)
grantha_mei_letters.extend(sanskrit_mei_letters)

grantha_agaram_letters = copy(agaram_letters)
grantha_agaram_letters.extend(sanskrit_letters)


uyirmei_letters = [
    u"ක", u"කා", u"කැ", u"කෑ", u"කි", u"කී", u"කු", u"කූ", u"කෘ", u"කෲ", u"කෟ", u"කෟෟ", u"කෙ", u"කේ", u"කෛ", u"කො", u"කෝ", u"කෞ",
    u"ඛ", u"ඛා", u"ඛැ", u"ඛෑ", u"ඛි", u"ඛී", u"ඛු", u"ඛූ", u"ඛෘ", u"ඛෘෘ", u"ඛෟ", u"ඛෟෟ", u"ඛෙ", u"ඛේ", u"ඛෛ", u"ඛො", u"ඛෝ", u"ඛෞ",
    u"ග", u"ගා", u"ගැ", u"ගෑ", u"ගි", u"ගී", u"ගු", u"ගූ", u"ගෘ", u"ගෘෘ", u"ගෟ", u"ගෟෟ", u"ගෙ", u"ගේ", u"ගෛ", u"ගො", u"ගෝ", u"ගෞ",
    u"ඝ", u"ඝා", u"ඝැ", u"ඝෑ", u"ඝි", u"ඝී", u"ඝු", u"ඝූ", u"ඝෘ", u"ඝෘෘ", u"ඝෟ", u"ඝෟෟ", u"ඝෙ", u"ඝේ", u"ඝෛ", u"ගො", u"ඝෝ", u"ඝෞ",
    u"ඞ", u"ඞා", u"ඞැ", u"ඞෑ", u"ඞි", u"ඞී", u"ඞු", u"ඞූ", u"ඞෘ", u"ඞෲ", u"ඞෟ", u"ඞෟෟ", u"ඞෙ", u"ඞේ", u"ඞෙෙ", u"ඞො", u"ඞෝ", u"ඝෞ",
    u"ඟ", u"ඟා", u"ඟැ", u"ඟෑ", u"ඟි", u"ඟී", u"ඟු", u"ඟූ", u"ඟෘ", u"ඟෘෘ", u"ඟෟ", u"ඟෟෟ", u"ඟෙ", u"ඟේ", u"ඟෛ", u"ඟො", u"ඟෝ", u"ඟෞ",
    u"ච", u"චා", u"චැ", u"චෑ", u"චි", u"චී", u"චු", u"චූ", u"චෘ", u"චෘෘ", u"චෟ", u"චෟෟ", u"චෙ", u"චේ", u"චෛ", u"චො", u"චෝ", u"චෞ",
    u"ඡ", u"ඡා", u"ඡැ", u"ඡෑ", u"ඡි", u"ඡී", u"ඡු", u"ඡූ", u"ඡෘ", u"ඡෘෘ", u"ඡෟ", u"ඡෟෟ", u"ඡෙ", u"ඡේ", u"ඡෛ", u"ඡො", u"ඡෝ", u"ඡෞ",
    u"ජ", u"ජා", u"ජැ", u"ජෑ", u"ජි", u"ජී", u"ජු", u"ජූ", u"ජෘ", u"ජෘෘ", u"ජෟ", u"ජෟෟ", u"ජෙ", u"ජේ", u"ජෛ", u"ජො", u"ජෝ", u"ජෞ",
    u"ඣ", u"ඣා", u"ඣැ", u"ඣෑ", u"ඣි", u"ඣී", u"ඣු", u"ඣූ", u"ඣෘ", u"ඣෘෘ", u"ඣෟ", u"ඣෟෟ", u"ඣෙ", u"ඣේ", u"ඣෛ", u"ඣො", u"ඣෝ", u"ඣෞ",
    u"ඤ", u"ඤා", u"ඤැ", u"ඤෑ", u"ඤි", u"ඤී", u"ඤු", u"ඤූ", u"ඤෘ", u"ඤෘෘ", u"ඤෟ", u"ඤෟෟ", u"ඤෙ", u"ඤේ", u"ඤෛ", u"ඤො", u"ඤෝ", u"ඤෞ",
    u"ට", u"ටා", u"ටැ", u"ටෑ", u"ටි", u"ටී", u"ටු", u"ටූ", u"ටෘ", u"ටෘෘ", u"ටෟ", u"ටෟෟ", u"ටෙ", u"ටේ", u"ටෛ", u"ටො", u"ටෝ", u"ටෞ",
    u"ඨ", u"ඨා", u"ඨැ", u"ඨෑ", u"ඨි", u"ඨී", u"ඨු", u"ඨූ", u"ඨෘ", u"ඨෘෘ", u"ඨෟ", u"ඨෟෟ", u"ඨෙ", u"ඨේ", u"ඨෛ", u"ඨො", u"ඨෝ", u"ඨෞ",
    u"ඪ", u"ඪා", u"ඪැ", u"ඪෑ", u"ඪි", u"ඪී", u"ඪු", u"ඪූ", u"ඪෘ", u"ඪෘෘ", u"ඪෟ", u"ඪෟෟ", u"ඪෙ", u"ඪේ", u"ඪෛ", u"ඪො", u"ඪෝ", u"ඪෞ",
    u"ණ", u"ණා", u"ණැ", u"ණෑ", u"ණි", u"ණී", u"ණු", u"ණූ", u"ණෘ", u"ණෘෘ", u"ණෟ", u"ණෟෟ", u"ණෙ", u"ණේ", u"ණෛ", u"ණො", u"ණෝ", u"ණෞ",
    u"ඬ", u"ඬා", u"ඬැ", u"ඬෑ", u"ඬි", u"ඬී", u"ඬු", u"ඬූ", u"ඬෘ", u"ඬෘෘ", u"ඬෟ", u"ඬෟෟ", u"ඬෙ", u"ඬේ", u"ඬෛ", u"ඬො", u"ඬෝ", u"ඬෞ",
    u"ත", u"තා", u"තැ", u"තෑ", u"ති", u"තී", u"තු", u"තූ", u"තෘ", u"තෘෘ", u"තෟ", u"තෟෟ", u"තෙ", u"තේ", u"තෛ", u"තො", u"තෝ", u"තෞ",
    u"ථ", u"ථා", u"ථැ", u"ථෑ", u"ථි", u"ථී", u"ථු", u"ථූ", u"ථෘ", u"ථෘෘ", u"ථෟ", u"ථෟෟ", u"ථෙ", u"ථේ", u"ථෛ", u"ථො", u"ථෝ", u"ථෞ",
    u"ද", u"දා", u"දැ", u"දෑ", u"දි", u"දී", u"දු", u"දූ", u"දෘ", u"දෘෘ", u"දෟ", u"දෟෟ", u"දෙ", u"දේ", u"දෛ", u"දො", u"දෝ", u"දෞ",
    u"ධ", u"ධා", u"ධැ", u"ධෑ", u"ධි", u"ධී", u"ධු", u"ධූ", u"ධෘ", u"ධෘෘ", u"ධෟ", u"ධෟෟ", u"ධෙ", u"ධේ", u"ධෛ", u"ධො", u"ධෝ", u"ධෞ",
    u"න", u"නා", u"නැ", u"නෑ", u"නි", u"නී", u"නු", u"නූ", u"නෘ", u"නෘෘ", u"නෟ", u"නෟෟ", u"නෙ", u"නේ", u"නෛ", u"නො", u"නෝ", u"නෞ",
    u"ඳ", u"ඳා", u"ඳැ", u"ඳෑ", u"ඳි", u"ඳී", u"ඳු", u"ඳූ", u"ඳෘ", u"ඳෘෘ", u"ඳෟ", u"ඳෟෟ", u"ඳෙ", u"ඳේ", u"ඳෛ", u"ඳො", u"ඳෝ", u"ඳෞ",
    u"ප", u"පා", u"පැ", u"පෑ", u"පි", u"පී", u"පු", u"පූ", u"පෘ", u"පෘෘ", u"පෟ", u"පෟෟ", u"පෙ", u"පේ", u"පෛ", u"පො", u"පෝ", u"පෞ",
    u"ඵ", u"ඵා", u"ඵැ", u"ඵෑ", u"ඵි", u"ඵී", u"ඵු", u"ඵූ", u"ඵෘ", u"ඵෘෘ", u"ඵෟ", u"ඵෟෟ", u"ඵෙ", u"ඵේ", u"ඵෛ", u"ඵො", u"ඵෝ", u"ඵෞ",
    u"බ", u"බා", u"බැ", u"බෑ", u"බි", u"බී", u"බු", u"බූ", u"බෘ", u"බෘෘ", u"බෟ", u"බෟෟ", u"බෙ", u"බේ", u"බෛ", u"බො", u"බෝ", u"පෞ",
    u"භ", u"භා", u"භැ", u"භෑ", u"භි", u"භී", u"භු", u"භූ", u"භෘ", u"භෘෘ", u"භෟ", u"භෟෟ", u"භෙ", u"භේ", u"භෛ", u"භො", u"භෝ", u"භෞ",
    u"ම", u"මා", u"මැ", u"මෑ", u"මි", u"මී", u"මු", u"මූ", u"මෘ", u"මෘෘ", u"මෟ", u"මෟෟ", u"මෙ", u"මේ", u"මෛ", u"මො", u"මෝ", u"මෞ",
    u"ඹ", u"ඹා", u"ඹැ", u"ඹෑ", u"ඹි", u"ඹී", u"ඹු", u"ඹූ", u"ඹෘ", u"ඹෘෘ", u"ඹෟ", u"ඹෟෟ", u"ඹෙ", u"ඹේ", u"ඹෛ", u"ඹො", u"ඹෝ", u"ඹෞ",
    u"ය", u"යා", u"යැ", u"යෑ", u"යි", u"යී", u"යු", u"යූ", u"යෘ", u"යෘෘ", u"යෟ", u"යෟෟ", u"යෙ", u"යේ", u"යෛ", u"යො", u"යෝ", u"යෞ",
    u"ර", u"රා", u"රැ", u"රෑ", u"රි", u"රී", u"රු", u"රූ", u"රෘ", u"රෘෘ", u"රෟ", u"රෟෟ", u"රෙ", u"රේ", u"රෛ", u"රො", u"රෝ", u"රෞ",
    u"ල", u"ලා", u"ලැ", u"ලෑ", u"ලි", u"ලී", u"ලු", u"ලූ", u"ලෘ", u"ලෘෘ", u"ලෟ", u"ලෟෟ", u"ලෙ", u"ලේ", u"ලෛ", u"ලො", u"ලෝ", u"ලෞ",
    u"ව", u"වා", u"වැ", u"වෑ", u"වි", u"වී", u"වු", u"වූ", u"වෘ", u"වෘෘ", u"වෟ", u"වෟෟ", u"වෙ", u"වේ", u"වෛ", u"වො", u"වෝ", u"වෞ",
    u"ශ", u"ශා", u"ශැ", u"ශෑ", u"ශි", u"ශී", u"ශු", u"ශූ", u"ශෘ", u"ශෘෘ", u"ශෟ", u"ශෟෟ", u"ශෙ", u"ශේ", u"ශෛ", u"ශො", u"ශෝ", u"ශෞ",
    u"ෂ", u"ෂා", u"ෂැ", u"ෂෑ", u"ෂි", u"ෂී", u"ෂු", u"ෂූ", u"ෂෘ", u"ෂෘෘ", u"ෂෟ", u"ෂෟෟ", u"ෂෙ", u"ෂේ", u"ෂෛ", u"ෂො", u"ෂෝ", u"ෂෞ",
    u"ස", u"සා", u"සැ", u"සෑ", u"සි", u"සී", u"සු", u"සූ", u"සෘ", u"සෘෘ", u"සෟ", u"සෟෟ", u"සෙ", u"සේ", u"සෛ", u"සො", u"සෝ", u"සෞ",
    u"හ", u"හා", u"හැ", u"හෑ", u"හි", u"හී", u"හු", u"හූ", u"හෘ", u"හෘෘ", u"හෟ", u"හෟෟ", u"හෙ", u"හේ", u"හෛ", u"හො", u"හෝ", u"හෞ",
    u"ළ", u"ළා", u"ළැ", u"ළෑ", u"ළි", u"ළී", u"ළු", u"ළූ", u"ළෘ", u"ළෘෘ", u"ළෟ", u"ළෟෟ", u"ළෙ", u"ළේ", u"ළෛ", u"ළො", u"ළෝ", u"ළෞ",
    u"ෆ", u"ෆා", u"ෆැ", u"ෆෑ", u"ෆි", u"ෆී", u"ෆු", u"ෆූ", u"ෆෘ", u"ෆෘෘ", u"ෆෟ", u"ෆෟෟ", u"ෆෙ", u"ෆේ", u"ෆෛ", u"ෆො", u"ෆෝ", u"ෆෞ"
]

# constants
TA_UYIR_LEN = len(uyir_letters)
TA_MEI_LEN = len(mei_letters)
TA_AGARAM_LEN = len(agaram_letters)
TA_UYIRMEI_LEN = len(uyirmei_letters)

# Ref: https://en.wikipedia.org/wiki/Tamil_numerals
# tamil digits : Apart from the numerals (0-9), Tamil also has numerals for 10, 100 and 1000.
tamil_digit_1to10 = [u"௦", u"௧", u"௨", u"௩",
                     u"௪", u"௫", u"௬", u"௭", u"௮", u"௯", u"௰"]
tamil_digit_100 = u"௱"
tamil_digit_1000 = u"௲"

tamil_digits = [(num, digit)
                for num, digit in zip(range(0, 11), tamil_digit_1to10)]
tamil_digits.extend([(100, tamil_digit_100), (1000, tamil_digit_1000)])

# tamil symbols
_day = u"௳"
_month = u"௴"
_year = u"௵"
_debit = u"௶"
_credit = u"௷"
_rupee = u"௹"
_numeral = u"௺"
_sri = u"\u0bb6\u0bcd\u0bb0\u0bc0"  # SRI - ஶ்ரீ
_ksha = u"\u0b95\u0bcd\u0bb7"  # KSHA - க்ஷ
_ksh = u"\u0b95\u0bcd\u0bb7\u0bcd"  # KSH - க்ஷ்

tamil_symbols = [_day, _month, _year, _debit,
                 _credit, _rupee, _numeral, _sri, _ksha, _ksh]

# total tamil letters in use, including sanskrit letters
tamil_letters = uyir_letters + uyirmei_letters + \
    agaram_letters + mei_letters + [ayudha_letter]

# grantha_uyirmei_letters = copy(tamil_letters[tamil_letters.index(u"கா") - 1:])
grantha_uyirmei_letters = copy(uyirmei_letters)

# length of the definitions


def uyir_len():
    return TA_UYIR_LEN  # 12


def mei_len():
    return TA_MEI_LEN  # 18


def agaram_len():
    return TA_AGARAM_LEN  # 18


def uyirmei_len():
    return TA_UYIRMEI_LEN  # 216


def tamil_len():
    return len(tamil_letters)

# access the letters


def uyir(idx):
    assert (idx >= 0 and idx < uyir_len())
    return uyir_letters[idx]


def agaram(idx):
    assert (idx >= 0 and idx < agaram_len())
    return agaram_letters[idx]


def mei(idx):
    assert (idx >= 0 and idx < mei_len())
    return mei_letters[idx]


def uyirmei(idx):
    assert(idx >= 0 and idx < uyirmei_len())
    return uyirmei_letters[idx]


def mei_to_agaram(in_syllable):
    if in_syllable in grantha_mei_letters:
        mei_pos = grantha_mei_letters.index(in_syllable)
        agaram_a_pos = 0
        syllable = uyirmei_constructed(mei_pos, agaram_a_pos)
        return syllable
    return in_syllable


def uyirmei_constructed(mei_idx, uyir_idx):
    """ construct uyirmei letter give mei index and uyir index """
    idx, idy = mei_idx, uyir_idx
    assert (idy >= 0 and idy < uyir_len())
    assert (idx >= 0 and idx < 6 + mei_len())
    return grantha_agaram_letters[mei_idx] + accent_symbols[uyir_idx]


def tamil(idx):
    """ retrieve Tamil letter at canonical index from array utf8.tamil_letters """
    assert (idx >= 0 and idx < tamil_len())
    return tamil_letters[idx]

# companion function to @tamil()


def getidx(letter):
    for itr in range(0, tamil_len()):
        if tamil_letters[itr] == letter:
            return itr
    raise Exception("Cannot find letter in Tamil arichuvadi")

# useful part of the API:


def istamil_prefix(word):
    """ check if the given word has a tamil prefix. Returns
    either a True/False flag """
    for letter in tamil_letters:
        if (word.find(letter) == 0):
            return True
    return False


if not PYTHON3:
    def is_tamil_unicode_predicate(
        x): return x >= unichr(2946) and x <= unichr(3066)
else:
    def is_tamil_unicode_predicate(x): return x >= chr(2946) and x <= chr(3066)


def is_tamil_unicode(sequence):
    # Ref: languagetool-office-extension/src/main/java/org/languagetool/openoffice/TamilDetector.java
    if type(sequence) is list:
        return list(map(is_tamil_unicode_predicate, sequence))
    if len(sequence) > 1:
        return list(map(is_tamil_unicode_predicate, get_letters(sequence)))
    return is_tamil_unicode_predicate(sequence)


def all_tamil(word_in):
    """ predicate checks if all letters of the input word are Tamil letters """
    if isinstance(word_in, list):
        word = word_in
    else:
        word = get_letters(word_in)
    return all([(letter in tamil_letters and letter != 'x') for letter in word])


def has_tamil(word):
    """check if the word has any occurance of any tamil letter """
    # list comprehension is not necessary - we bail at earliest
    for letters in tamil_letters:
        if (word.find(letters) >= 0):
            return True
    return False


def istamil(tchar):
    """ check if the letter tchar is prefix of
    any of tamil-letter. It suggests we have a tamil identifier"""
    if (tchar in tamil_letters):
        return True
    return False


def istamil_alnum(tchar):
    """ check if the character is alphanumeric, or tamil.
    This saves time from running through istamil() check. """
    return (tchar.isalnum() or istamil(tchar))


def reverse_word(word):
    """ reverse a Tamil word according to letters not unicode-points """
    op = get_letters(word)
    op.reverse()
    return u"".join(op)

# find out if the letters like, "பொ" are written in canonical "ப + ொ"" graphemes then
# return True. If they are written like "ப + ெ + ா" then return False on first occurrence


def is_normalized(text):
    # print(text[0],text[1],text[2],text[-1],text[-2])
    TLEN, idx = len(text), 1
    kaal = u"ா"
    Laa = u"ள"
    sinna_kombu, periya_kombu = u"ெ", u"ே"
    kombugal = [sinna_kombu, periya_kombu]

    # predicate measures if the normalization is violated
    def predicate(last_letter, prev_letter):
        if ((kaal == last_letter) and (prev_letter in kombugal)):
            return True
        if ((Laa == last_letter) and (prev_letter == sinna_kombu)):
            return True
        return False
    if TLEN < 2:
        return True
    elif TLEN == 2:
        if predicate(text[-1], text[-2]):
            return False
        return True
    idx = TLEN
    a = text[idx - 2]
    b = text[idx - 1]
    while (idx >= 0):
        if predicate(b, a):
            return False
        b = a
        idx = idx - 1
        if idx >= 0:
            a = text[idx]
    return True


def _make_set(args):
    args = list(filter(lambda x: x != '\u200d', args))
    if PYTHON3:
        return frozenset(args)
    return set(args)


grantha_agaram_set = _make_set(grantha_agaram_letters)
accent_symbol_set = _make_set(accent_symbols)
# accent_symbol_set_p = _make_set(accent_symbols_p)
uyir_letter_set = _make_set(uyir_letters)

# Split a tamil-unicode stream into
# tamil characters (individuals).


def get_letters(word):
    """ splits the word into a character-list of tamil/english
    characters present in the stream """
    word = word.strip()
    word = word.replace('.', '')
    ta_letters = list()
    not_empty = False
    WLEN, idx = len(word), 0
    while (idx < WLEN):
        c = word[idx]
        # print(idx,hex(ord(c)),len(ta_letters))
        if c in uyir_letter_set or c == ayudha_letter:
            ta_letters.append(c)
            not_empty = True
        elif c in grantha_agaram_set:
            ta_letters.append(c)
            not_empty = True
        elif c in accent_symbol_set:
            if not not_empty:
                # odd situation
                ta_letters.append(c)
                not_empty = True
            else:
                # print("Merge/accent")
                ta_letters[-1] = ta_letters[-1] + c
                # print(ta_letters[-1])
        elif c == pulli_symbols[0]:
            ta_letters[-1] += c
        else:
            if ord(c) < 256 or not (is_tamil_unicode(c)):
                ta_letters.append(c)
            else:
                if not_empty:
                    # print("Merge/??")
                    ta_letters[-1] += c
                else:
                    ta_letters.append(c)
                    not_empty = True
        idx = idx + 1
    return list(filter(lambda x: x != '\u200d', ta_letters))


_all_symbols = copy(accent_symbols)
_all_symbols.extend(pulli_symbols)
all_symbol_set = _make_set(_all_symbols)

# same as get_letters but use as iterable


def get_letters_iterable(word):
    """ splits the word into a character-list of tamil/english
    characters present in the stream """
    WLEN, idx = len(word), 0

    while (idx < WLEN):
        c = word[idx]
        # print(idx,hex(ord(c)),len(ta_letters))
        if c in uyir_letter_set or c == ayudha_letter:
            idx = idx + 1
            yield c
        elif c in grantha_agaram_set:
            if idx + 1 < WLEN and word[idx + 1] in all_symbol_set:
                c2 = word[idx + 1]
                idx = idx + 2
                yield (c + c2)
            else:
                idx = idx + 1
                yield c
        else:
            idx = idx + 1
            yield c
    return


grantha_uyirmei_splits = {}
for _uyir_idx in range(0, 18):
    for _mei_idx, _mei in enumerate(grantha_mei_letters):
        _uyirmei = uyirmei_constructed(_mei_idx, _uyir_idx)
        grantha_uyirmei_splits[_uyirmei] = [_mei, uyir_letters[_uyir_idx]]


def get_letters_elementary_iterable(word):
    for letter in get_letters_iterable(word):
        letter_parts = grantha_uyirmei_splits.get(letter, None)
        if letter_parts:
            yield letter_parts[0]
            yield letter_parts[1]
        else:
            yield letter
    return


def get_letters_elementary(word):
    rval = []
    word = word.strip()
    word = word.replace('.', '')
    for letter in get_letters(word):
        letter_parts = grantha_uyirmei_splits.get(letter, None)
        if letter_parts:
            rval.append(letter_parts[0])
            rval.append(letter_parts[1])
        else:
            rval.append(letter)
    return rval


def get_words(letters, tamil_only=False):
    return [word for word in get_words_iterable(letters, tamil_only)]


def get_words_iterable(letters, tamil_only=False):
    """ given a list of UTF-8 letters section them into words, grouping them at spaces """

    # correct algorithm for get-tamil-words
    buf = []
    for idx, let in enumerate(letters):
        if not let.isspace():
            if istamil(let) or (not tamil_only):
                buf.append(let)
        else:
            if len(buf) > 0:
                yield u"".join(buf)
                buf = []
    if len(buf) > 0:
        yield u"".join(buf)


def get_tamil_words(letters):
    """ reverse a Tamil word according to letters, not unicode-points """
    if not isinstance(letters, list):
        raise Exception(
            "metehod needs to be used with list generated from 'tamil.utf8.get_letters(...)'")
    return [word for word in get_words_iterable(letters, tamil_only=True)]


if PYTHON3:
    def cmp(x, y):
        if x == y:
            return 0
        if x > y:
            return 1
        return -1

# answer if word_a ranks ahead of, or at same level, as word_b in a Tamil dictionary order...
# for use with Python : if a > 0


def compare_words_lexicographic(word_a, word_b):
    """ compare words in Tamil lexicographic order """
    # sanity check for words to be all Tamil
    if (not all_tamil(word_a)) or (not all_tamil(word_b)):
        # print("## ")
        # print(word_a)
        # print(word_b)
        # print("Both operands need to be Tamil words")
        pass
    La = len(word_a)
    Lb = len(word_b)
    all_TA_letters = u"".join(tamil_letters)
    for itr in range(0, min(La, Lb)):
        pos1 = all_TA_letters.find(word_a[itr])
        pos2 = all_TA_letters.find(word_b[itr])

        if pos1 != pos2:
                    # print  not( pos1 > pos2), pos1, pos2
            return cmp(pos1, pos2)

    # result depends on if La is shorter than Lb, or 0 if La == Lb  i.e. cmp
    return cmp(La, Lb)

# return a list of ordered-pairs containing positions
# that are common in word_a, and word_b; e.g.
# தேடுக x தடங்கல் -> one common letter க [(2,3)]
# சொல் x   தேடுக -> no common letters []


def word_intersection(word_a, word_b):
    """ return a list of tuples where word_a, word_b intersect """
    positions = []
    word_a_letters = get_letters(word_a)
    word_b_letters = get_letters(word_b)
    for idx, wa in enumerate(word_a_letters):
        for idy, wb in enumerate(word_b_letters):
            if (wa == wb):
                positions.append((idx, idy))
    return positions


def unicode_normalize(cplxchar):
    Laa = u"ள"
    kaal = u"ா"
    sinna_kombu_a = u"ெ"
    periya_kombu_aa = u"ே"
    sinna_kombu_o = u"ொ"
    periya_kombu_oo = u"ோ"
    kombu_ak = u"ௌ"

    lcplx = len(cplxchar)
    if lcplx >= 3 and cplxchar[-1] == Laa:
        if cplxchar[-2] == sinna_kombu_a:
            return (cplxchar[:-2] + kombu_ak)
    if lcplx >= 2 and cplxchar[-1] == kaal:
        if cplxchar[-2] == sinna_kombu_a:
            return (cplxchar[:-2] + sinna_kombu_o)
        if cplxchar[-2] == periya_kombu_aa:
            return (cplxchar[:-2] + periya_kombu_oo)
    # no-op
    return cplxchar


def splitMeiUyir(uyirmei_char):
    """
    This function split uyirmei compound character into mei + uyir characters
    and returns in tuple.

    Input : It must be unicode tamil char.

    Written By : Arulalan.T
    Date : 22.09.2014

    """

    if not isinstance(uyirmei_char, PYTHON3 and str or unicode):
        raise ValueError("Passed input letter '%s' must be unicode, \
                                not just string" % uyirmei_char)

    if uyirmei_char in mei_letters or uyirmei_char in uyir_letters or uyirmei_char in ayudha_letter:
        return uyirmei_char

    if uyirmei_char not in grantha_uyirmei_letters:
        if not is_normalized(uyirmei_char):
            norm_char = unicode_normalize(uyirmei_char)
            rval = splitMeiUyir(norm_char)
            return rval
        raise ValueError(
            "Passed input letter '%s' is not tamil letter" % uyirmei_char)

    idx = grantha_uyirmei_letters.index(uyirmei_char)
    uyiridx = idx % 12
    meiidx = int((idx - uyiridx) / 12)
    return (grantha_mei_letters[meiidx], uyir_letters[uyiridx])
# end of def splitMeiUyir(uyirmei_char):


def joinMeiUyir(mei_char, uyir_char):
    """
    This function join mei character and uyir character, and retuns as
    compound uyirmei unicode character.

    Inputs:
        mei_char : It must be unicode tamil mei char.
        uyir_char : It must be unicode tamil uyir char.

    Written By : Arulalan.T
    Date : 22.09.2014
    """
    if not isinstance(mei_char, PYTHON3 and str or unicode):
        raise ValueError("Passed input mei character '%s' must be unicode, \
                                not just string" % mei_char)
    if not isinstance(uyir_char, PYTHON3 and str or unicode):
        raise ValueError("Passed input uyir character '%s' must be unicode, \
                                not just string" % uyir_char)
    if mei_char not in grantha_mei_letters:
        raise ValueError("Passed input character '%s' is not a"
                         "tamil mei character" % mei_char)
    if uyir_char not in uyir_letters:
        raise ValueError("Passed input character '%s' is not a"
                         "tamil uyir character" % uyir_char)
    uyiridx = uyir_letters.index(uyir_char)
    meiidx = grantha_mei_letters.index(mei_char)
    # calculate uyirmei index
    uyirmeiidx = meiidx * 18 + uyiridx
    return grantha_uyirmei_letters[uyirmeiidx]


def print_tamil_words(tatext, use_frequencies=False):
    taletters = get_letters(tatext)
    # for word in re.split(u"\s+",tatext):
    #    print(u"-> ",word)
    # tamil words only
    frequency = {}
    for pos, word in enumerate(get_tamil_words(taletters)):
        frequency[word] = 1 + frequency.get(word, 0)
    # for key in frequency.keys():
    #    print(u"%s : %s"%(frequency[key],key))
    # sort words by descending order of occurence
    for l in sorted(frequency.iteritems(), key=operator.itemgetter(1)):
        if use_frequencies:
            print(u"%d -> %s" % (l[1], l[0]))
        else:
            print(u"%s" % l[0])


def tamil_sorted(list_data):
    if PYTHON3:
        asorted = sorted(list_data, key=functools.cmp_to_key(
            compare_words_lexicographic))
    else:
        asorted = sorted(list_data, cmp=compare_words_lexicographic)
    return asorted

# Tamil Letters
# அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ ஃ
# க் ச் ட் த் ப் ற் ஞ் ங் ண் ந் ம் ன் ய் ர் ல் வ் ழ் ள் ஜ் ஷ் ஸ் ஹ்
# க ச ட த ப ற ஞ ங ண ந ம ன ய ர ல வ ழ ள ஜ ஷ ஸ ஹ
# க கா கி கீ கு கூ கெ கே கை  கௌ
# ச சா சி சீ சு சூ செ சே சை சொ சோ சௌ
# ட டா டி டீ டு டூ டெ டே டை டொ டோ டௌ
# த தா தி தீ து தூ தெ தே தை தொ தோ தௌ
# ப பா பி பீ பு பூ பெ பே பை பொ போ பௌ
# ற றா றி றீ று றூ றெ றே றை றொ றோ றௌ
# ஞ ஞா ஞி ஞீ ஞு ஞூ ஞெ ஞே ஞை ஞொ ஞோ ஞௌ
# ங ஙா ஙி ஙீ ஙு ஙூ ஙெ ஙே ஙை ஙொ ஙோ ஙௌ
# ண ணா ணி ணீ ணு ணூ ணெ ணே ணை ணொ ணோ ணௌ
# ந நா நி நீ நு நூ நெ நே நை நொ நோ நௌ
# ம மா மி மீ மு மூ மெ மே மை மொ மோ மௌ
# ன னா னி னீ னு னூ னெ னே னை னொ னோ னௌ
# ய யா யி யீ யு யூ யெ யே யை யொ யோ யௌ
# ர ரா ரி ரீ ரு ரூ ரெ ரே ரை ரொ ரோ ரௌ
# ல லா லி லீ லு லூ லெ லே லை லொ லோ லௌ
# வ வா வி வீ வு வூ வெ வே வை வொ வோ வௌ
# ழ ழா ழி ழீ ழு ழூ ழெ ழே ழை ழொ ழோ ழௌ
# ள ளா ளி ளீ ளு ளூ ளெ ளே ளை ளொ ளோ ளௌ
# ஶ ஶா ஶி ஶீ 	ஶு 	ஶூ 	ஶெ 	ஶே 	ஶை ஶொ ஶோ ஶௌ
# ஜ ஜா ஜி ஜீ ஜு ஜூ ஜெ ஜே ஜை ஜொ ஜோ ஜௌ
# ஷ ஷா ஷி ஷீ ஷு ஷூ ஷெ ஷே ஷை ஷொ ஷோ ஷௌ
# ஸ ஸா ஸி ஸீ ஸு ஸூ ஸெ ஸே ஸை ஸொ ஸோ ஸௌ
# ஹ ஹா ஹி ஹீ ஹு ஹூ ஹெ ஹே ஹை ஹொ ஹோ ஹௌ
# க்ஷ க்ஷா க்ஷி க்ஷீ க்ஷு க்ஷூ க்ஷெ க்ஷே க்ஷை க்ஷொ க்ஷோ க்ஷௌ
