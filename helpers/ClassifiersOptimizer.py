from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import confusion_matrix
from config import Config


class ClassifierOptimizer:

    def __init__(self):
        self.best_model = None

    def evaluate(self, classifiers, x, y, filename="model/best-model.pkl"):
        x_train, x_test, y_train, y_test = train_test_split(x, y, )
        best_score = 0

        for classifier in classifiers:
            model, training_duration = classifier.classify(x_train, y_train)

            test_score = model.score(x_test, y_test)
            train_score = model.score(x_train, y_train)

            if test_score > best_score:
                self.best_model = model

            print("Results for {0}:".format(classifier.name))
            print(" train set accuracy: %0.3f" % train_score)
            print(" test set accuracy: %0.3f" % test_score)
            print(" training time: %0.3f seconds" % training_duration)
            print("\n")

        print("Best model confusion matrix for test data:")
        print(confusion_matrix(y_test, self.best_model.predict(x_test)))
        print("\n")

        best_model_prediction_probability = [max(x) for x in self.best_model.predict_proba(x_test)]
        x_test_threshold = [x for x, z in zip(x_test, best_model_prediction_probability) if z >= Config.SCORING_THRESHOLD]
        y_test_threshold = [y for y, z in zip(y_test, best_model_prediction_probability) if z >= Config.SCORING_THRESHOLD]
        print("Best model score on test set for defined threshold({0}) is {1} with {2}% examples covered".format(
            Config.SCORING_THRESHOLD,
            self.best_model.score(x_test_threshold, y_test_threshold),
            len(x_test_threshold) / float(len(x_test))
        ))

        pickle.dump(self.best_model, open(filename, 'wb'))


