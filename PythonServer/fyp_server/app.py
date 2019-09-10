from flask import Flask, request, jsonify, send_from_directory
import modules.main.english.english as main_en
import modules.lang_identifier.lang_identifier as lang_identifier
from flask_cors import CORS

app = Flask(__name__, static_url_path='')
CORS(app)


@app.route('/')
def hello_world():
    return '<h1 align="center">Welcome to  Thesaurus REST API !</h1>'


@app.route('/thesaurus', methods=['GET', "POST"])
def thesaurus():
    requestData = request.get_json(force=True)
    input_word = requestData['word']
    input_lang = requestData['lang']
    if input_lang == "en":
        response_body = main_en.getData(input_word)
        return jsonify(response_body)
    else:
        response_body = main_en.getData(input_word)
        return jsonify(response_body)


@app.route('/language', methods=["POST"])
def lang_predict():
    request_data = request.get_json(force=True)
    input_word = request_data['word']
    lang = lang_identifier.predict_lang(input_word)
    response_body = {
        "lang": lang
    }
    return jsonify(response_body)


@app.route('/readword')
def data():
    word = request.args.get('word')
    response = send_from_directory('modules/tts/audio_db', word + '.mp3')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
