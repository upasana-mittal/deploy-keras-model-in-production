import pickle
import tensorflow as tf

class SentimentService(object):
    model1 = None
    tokenizer = None

    @classmethod
    def load_deep_model(self, model):
        loaded_model = tf.keras.models.load_model("./src/mood-saved-models/" + model + ".h5")
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


