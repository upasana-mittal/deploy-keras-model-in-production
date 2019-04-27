from keras.models import model_from_json
import pickle

class SentimentService(object):
    model1 = None  # Where we keep the model when it's loaded

    @classmethod
    def load_deep_model(cls, model):
        json_file = open('src/mood-saved-models/' + model + '.json', 'r')
        loaded_model_json = json_file.read()
        loaded_model = model_from_json(loaded_model_json)

        loaded_model.load_weights("src/mood-saved-models/" + model + ".h5")

        loaded_model._make_predict_function()
        return loaded_model

    @classmethod
    def get_model1(cls):
        """Get the model object for this instance, loading it if it's not already loaded."""
        if cls.model1 is None:
            cls.model1 = cls.load_deep_model('model5_ver1')
        return cls.model1

    @classmethod
    def load_tokenizer(cls):
        with open('src/mood-saved-models/tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)
        return tokenizer


