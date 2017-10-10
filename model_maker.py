from helpers.ClassifiersOptimizer import *
from helpers.Classifier import Classifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import SGDClassifier
import pandas as pd

CLASSIFIERS = [
    Classifier("Multinomial_naive_bayes", MultinomialNB(), {"clf__alpha": [.01, .1, .5, 1.0]}),
    Classifier("Bernoulli_naive_bayes", BernoulliNB(), {"clf__alpha": [.01, .1, .5, 1.0]}),
    Classifier("SGD", SGDClassifier(loss='log'), {"clf__alpha": [.0001, .001], "clf__n_iter": [50], "clf__penalty": ["elasticnet"]})
]


def read_data(input_file):
    df = pd.read_csv(input_file)
    return df["TITLE"], df["CATEGORY"]


if __name__ == "__main__":
    ## read training data
    X, y = read_data('data/uci-news-aggregator.csv')

    ### find best model for document classification and store it using pickle
    co = ClassifierOptimizer()
    co.evaluate(CLASSIFIERS, X, y)