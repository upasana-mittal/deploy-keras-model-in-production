import json
import pandas as pd
from flask import Flask, request, abort, Response
from keras.preprocessing.sequence import pad_sequences
from service.textPreprocessing import TextPreprocessing
from keras import backend
from service.sentimentService import SentimentService

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/mood-detect', methods=['POST'])
def clean():

    if not request.json or not 'text' in request.json:
        abort(400)

    tp = TextPreprocessing()

    sent = pd.Series(request.json['text'])
    new_sent = [tp.tweet_preprocessing(i) for i in sent]

    seq = SentimentService.load_tokenizer().texts_to_sequences(pd.Series(''.join(new_sent)))
    test = pad_sequences(seq, maxlen=256)

    with backend.get_session().graph.as_default() as g:
        model = SentimentService.get_model1()

    res = model.predict_proba(test,batch_size=32, verbose=0)

    lab_list = ['anger', 'disgust', 'fear', 'guilt', 'joy', 'sadness', 'shame']
    feats = {}
    for actual, probabilities in zip(lab_list, res[0]):
        feats[actual] = 100*probabilities

    return Response(json.dumps(feats), status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True,threaded=True, host='0.0.0.0')
