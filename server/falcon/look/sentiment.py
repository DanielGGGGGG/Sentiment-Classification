import json
import keras
import falcon
import pickle
import keras
import jieba
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

with open('look/tokenizer.pickle','rb') as handle:
    tokenizer = pickle.load(handle)

MAX_SENTENCE_LENGTH = 50
ml_model = load_model("look/api_test.h5")

class Resource(object):

    def on_get(self, req, resp):

        sentence = req.params['sentence']
        sequences = tokenizer.texts_to_sequences([" ".join(jieba.cut(sentence.strip() + " $ENDING$"))])
        data = pad_sequences(sequences, maxlen=MAX_SENTENCE_LENGTH)
        pred = ml_model.predict_proba(data)
        doc = {
            'KII_SCORE': 
                {
                    'SOCRE': float(pred[0][0]),
                    'Sentence': sentence,
                }
        }

        # Create a JSON representation of the resource
        resp.body = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200