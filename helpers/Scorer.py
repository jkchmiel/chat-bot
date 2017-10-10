import pickle


class Scorer:
    def __init__(self, filename):
        self.model = pickle.load(open(filename, 'rb'))

    def score(self, x):
        return self.model.predict(x)

    def score_all(self, x):
        return self.model.predict(x)[0], [max(x) for x in self.model.predict_proba(x)][0]

