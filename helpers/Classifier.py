from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from time import time


class Classifier:
    def __init__(self, name, clf, parameters):
        self.parameters = parameters
        self.name = name
        self.clf = clf
        self.model = None

    def classify(self, x_train, y_train):
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(stop_words='english')),
            ('clf', self.clf)
        ])
        model = GridSearchCV(pipeline, self.parameters, n_jobs=-1, verbose=0)
        t0 = time()
        model.fit(x_train, y_train)
        return model.best_estimator_, time() - t0


