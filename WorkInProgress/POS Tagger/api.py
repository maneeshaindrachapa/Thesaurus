from flask import Flask, jsonify, abort, request, json
import nltk
from util.preprocessing import addCharInformation, createMatrices, addCasingInformation
from util.preprocessing_sin import addCharInformation as addCharSinhala, addCasingInformation as addCasingSinhala,  createMatrices as createSinhala
from neuralnets.BiLSTM import BiLSTM
import sys

app = Flask(__name__)

tamil_ner = BiLSTM.loadModel('final/tamil/ner_model_level1.h5')
tamil_pos = BiLSTM.loadModel('final/tamil/tamil_pos.h5')
sinhala_pos = BiLSTM.loadModel('models/data_0.3603_0.4702_1.h5')
text = "பணிப்பாளர் நாயகம் ,"
sentences = [{'tokens': nltk.word_tokenize(
    sent)} for sent in nltk.sent_tokenize(text)]
addCharInformation(sentences)
addCasingInformation(sentences)
dataMatrix = createMatrices(sentences, tamil_ner.mappings, True)
tags = tamil_ner.tagSentences(dataMatrix)
tags = tamil_pos.tagSentences(dataMatrix)
tags = sinhala_pos.tagSentences(dataMatrix)


@app.route('/api/v1/ner/tamil', methods=['POST'])
def get_tamil_ner():
    text = request.form['sentence']
    sentences = [{'tokens': nltk.word_tokenize(
        text)}]
    addCharInformation(sentences)
    addCasingInformation(sentences)
    dataMatrix = createMatrices(sentences, tamil_ner.mappings, True)
    tags = tamil_ner.tagSentences(dataMatrix)
    for sentenceIdx in range(len(sentences)):
        tokens = sentences[sentenceIdx]['tokens']
        data = []
        for tokenIdx in range(len(tokens)):
            tokenTags = []
            for modelName in sorted(tags.keys()):
                tokenTags.append(tags[modelName][sentenceIdx][tokenIdx])
            data.append({'token': tokens[tokenIdx], 'tag': tokenTags})
    return jsonify({'data': data})


@app.route('/api/v1/pos/tamil', methods=['POST'])
def get_tamil_pos():
    text = request.form['sentence']
    sentences = [{'tokens': nltk.word_tokenize(
        text)}]
    addCharInformation(sentences)
    addCasingInformation(sentences)
    dataMatrix = createMatrices(sentences, tamil_pos.mappings, True)
    tags = tamil_pos.tagSentences(dataMatrix)
    for sentenceIdx in range(len(sentences)):
        tokens = sentences[sentenceIdx]['tokens']
        data = []
        for tokenIdx in range(len(tokens)):
            tokenTags = []
            for modelName in sorted(tags.keys()):
                tokenTags.append(tags[modelName][sentenceIdx][tokenIdx])

            data.append({'token': tokens[tokenIdx], 'tag': tokenTags})
    return jsonify({'data': data})


@app.route('/api/v1/pos/sinhala', methods=['POST'])
def get_sinhala_pos():
    text = request.form['sentence']
    sentences = [{'tokens': nltk.word_tokenize(
        text)}]
    addCharSinhala(sentences)
    addCasingSinhala(sentences)
    dataMatrix = createSinhala(sentences, sinhala_pos.mappings, True)
    tags = sinhala_pos.tagSentences(dataMatrix)
    for sentenceIdx in range(len(sentences)):
        tokens = sentences[sentenceIdx]['tokens']
        data = []
        for tokenIdx in range(len(tokens)):
            tokenTags = []
            for modelName in sorted(tags.keys()):
                tokenTags.append(tags[modelName][sentenceIdx][tokenIdx])

            data.append({'token': tokens[tokenIdx], 'tag': tokenTags})
    return jsonify({'data': data})


@app.route('/api/v1/', methods=['GET'])
def get_status():
    return 'Server is running'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
