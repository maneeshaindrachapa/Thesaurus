from flask import Flask, request, jsonify, send_from_directory
import modules.main.english.english as english
import modules.main.sinhala.sinhala as sinhala
import modules.formatter.formatter as formatter
import modules.api_docs.docs as apidocs
import modules.lang_identifier.lang_identifier as lang_identifier
from flask_cors import CORS

app = Flask(__name__, static_url_path='')
CORS(app)


@app.route('/')
def hello_world():
    return jsonify(apidocs.generateDoc())


@app.route('/thesaurus', methods=['GET', "POST"])
def thesaurus():
    requestData = request.get_json(force=True)
    input_word = requestData['word']
    input_lang = requestData['language']
    if input_lang == "en":
        response_code, response_data = english.getData(input_word)
        return jsonify(formatter.responseFormat(response_data, response_code))
    elif input_lang == "si":
        response_code, response_data = sinhala.getData(input_word)
        return jsonify(formatter.responseFormat(response_data,response_code))
    else:
        return jsonify(formatter.responseFormat("Not supported language", 405))


@app.route('/language', methods=["POST"])
def lang_predict():
    request_data = request.get_json(force=True)
    input_word = request_data['word']
    lang = lang_identifier.predict_lang(input_word)
    response_data = {
        "language": lang
    }
    return jsonify(formatter.responseFormat(response_data))


@app.route('/readword')
def data():
    word = request.args.get('word')
    response = send_from_directory('modules/tts/audio_db', word + '.mp3')
    return response



if __name__ == '__main__':
    app.run(host='0.0.0.0')
