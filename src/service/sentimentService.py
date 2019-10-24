from keras.models import model_from_json
import pickle

class SentimentService(object):
    model1 = None
    tokenizer = None

    @classmethod
    def load_deep_model(self, model):
        json_file = open('./src/mood-saved-models/' + model + '.json', 'r')
        loaded_model_json = json_file.read()
        loaded_model = model_from_json(loaded_model_json)

        loaded_model.load_weights("./src/mood-saved-models/" + model + ".h5")

        loaded_model._make_predict_function()
        return loaded_model

    @classmethod
    def get_model1(self):
        if self.model1 is None:
            self.model1 = self.load_deep_model('model5_ver1')
        return self.model1

    @classmethod
    def load_tokenizer(self):
        if self.tokenizer is None:
            with open('./src/mood-saved-models/tokenizer.pickle', 'rb') as handle:
                self.tokenizer = pickle.load(handle)
        return self.tokenizer


