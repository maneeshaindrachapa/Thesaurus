import os.path

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

import modules.api_docs.docs as apidocs
import modules.display_error.display_error as display_error
import modules.formatter.formatter as formatter
import modules.lang_identifier.lang_identifier as lang_identifier
import modules.main.english.english as english
import modules.main.sinhala.sinhala as sinhala
import modules.translator.translator as translator
import modules.tts.tts as tts
import modules.suggetions.suggetions as suggetions
import modules.spell_checker.spell_checker as spell_checker

app = Flask(__name__, static_url_path='')
CORS(app)


@app.route('/')
def docs():
    return jsonify(apidocs.generateDoc())


@app.route('/thesaurus', methods=['GET', "POST"])
def thesaurus():
    requestData = request.get_json(force=True)
    input_word = requestData['word']
    input_lang = requestData['language']
    if input_lang == "en":
        response_code, response_data = english.getData(input_word.replace('_', ' '))
        return jsonify(formatter.responseFormat(response_data, response_code))
    elif input_lang == "si":
        response_code, response_data = sinhala.getData(input_word)
        return jsonify(formatter.responseFormat(response_data, response_code))
    else:
        display_error.print_error(405, "Not supported language")
        return jsonify(formatter.responseFormat("Not supported language", 405))


@app.route('/language', methods=["POST"])
def lang_predict():
    request_data = request.get_json(force=True)
    input_word = request_data['word']
    response_code, lang = lang_identifier.predict_lang(input_word)
    response_data = {
        "language": lang
    }
    return jsonify(formatter.responseFormat(response_data, response_code))


## host/readword?word=<word>&lang=<lang>
@app.route('/readword')
def readword():
    word = request.args.get('word')
    lang = request.args.get('lang')

    if not os.path.isfile('modules/tts/audio_db' + word + '.mp3'):
        tts.audio_gen(word, lang)

    response = send_from_directory('modules/tts/audio_db', word + '.mp3')
    return response


## host/translate?word=<word>&lang=<lang>
@app.route('/translate')
def translate():
    word = request.args.get('word')
    src_lang = request.args.get('lang')

    lang_dict = {'si': 'en', 'en': 'si'}
    dest_lang = lang_dict[src_lang]

    response_code, response_data = translator.translate([word], src_lang, dest_lang)

    return jsonify(formatter.responseFormat(response_data, response_code))


## host/suggetion?word=<word>&wordCount=<count>
@app.route('/suggetion')
def suggetion():
    word = request.args.get('word')
    count = int(request.args.get('wordCount'))

    response_data = suggetions.suggest(word, count)

    return jsonify(formatter.responseFormat(response_data, 200))


## host/spellcheck?word=<word>&lang=<lang>
@app.route('/spellcheck')
def spellCheck():
    word = request.args.get('word')
    lang = request.args.get('lang')

    if lang == 'si':
        response_code, response_data = spell_checker.checkWord(word)

        return jsonify(formatter.responseFormat(response_data, response_code))
    else:
        return jsonify(formatter.responseFormat("Not supported language for spell checker", 404))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
