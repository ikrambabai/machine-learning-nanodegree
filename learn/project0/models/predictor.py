import pandas as pd


class Predictor(object):
    def __init__(self, name, rule, steps=None):
        self.name = name
        self.rule = rule
        self.predictions = None
        self.steps = steps

    def predict(self, data):
        predictions = []
        for _, passenger in data.iterrows():
            predictions.append(self.rule(passenger))
        self.predictions = pd.Series(predictions)

    def accuracy_score(self, truth):
        """ displays accuracy score for input truth and predictions. """
        if len(truth) == len(self.predictions):
            s = ((truth == self.predictions).mean() * 100).__round__(2)
            return {"scenario": self.name, "accuracy": s.__str__() + '%', "message": self.steps or "success"}

        else:
            return {"name": self.name, "accuracy": -1, "status": "error"}
