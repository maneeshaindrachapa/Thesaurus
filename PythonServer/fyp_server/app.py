from flask import Flask, request, render_template, jsonify, json
from service.english import *
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
    if(input_lang=="En"):
        synonyms = getSynonyms(input_word)
        definition = getDefinition(input_word)
        examples = getExamples(input_word)
        response_body = {
            "synonyms": synonyms,
            "definition": definition,
            "examples": examples
        }
        return jsonify(response_body)
    else:
        #Change below to sinhala
        synonyms = getSynonyms(input_word)
        definition = getDefinition(input_word)
        examples = getExamples(input_word)
        response_body = {
            "synonyms": synonyms,
            "definition": definition,
            "examples": examples
        }
        return jsonify(response_body)


    #return jsonify(content)

if __name__ == '__main__':
    app.run()
