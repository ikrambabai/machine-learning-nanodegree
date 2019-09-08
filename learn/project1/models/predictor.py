import pandas as pd


class Predictor(object):
    def __init__(self, name, rule):
        self.name = name
        self.rule = rule
        self.predictions = None

    def predict(self, data):
        predictions = []
        for _, passenger in data.iterrows():
            predictions.append(self.rule(passenger))
        self.predictions = pd.Series(predictions)

    def accuracy_score(self, truth):
        """ displays accuracy score for input truth and predictions. """
        if len(truth) == len(self.predictions):
            print("For scenario '{}', the predictions have an accuracy of {:.2f}%."
                  .format(self.name, (truth == self.predictions).mean() * 100))

        else:
            print("The # of predictions does not match number of outcomes!")
