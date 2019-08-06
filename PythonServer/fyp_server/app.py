from flask import Flask, request, jsonify
import modules.main.english as main_en
import modules.lang_identifier.lang_identifier as lang_identifier
import modules.translator.translator_v2 as translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/thesaurus', methods=['GET',"POST"])
def thesaurus():
    requestData = request.get_json(force=True)
    input_word = requestData['word']
    input_lang = requestData['lang']
    if(input_lang=="en"):
        synonyms = main_en.getSynonyms(input_word)
        definition = main_en.getDefinition(input_word)
        examples = main_en.getExamples(input_word)
        translated = translator.translate([x[0] for x in synonyms], 'en', 'si')
        response_body = {
            "synonyms": synonyms,
            "definition": definition,
            "examples": examples,
            "translated": translated
        }
        return jsonify(response_body)
    else:
        #Change below to sinhala
        synonyms = main_en.getSynonyms(input_word)
        definition = main_en.getDefinition(input_word)
        examples = main_en.getExamples(input_word)
        translated = translator.translate([x[0] for x in synonyms], 'si', 'en')
        response_body = {
            "synonyms": synonyms,
            "definition": definition,
            "examples": examples,
            "translated": translated
        }
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


if __name__ == '__main__':
    app.run()
