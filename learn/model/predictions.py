import pandas as pd


class Prediction(object):
    def __init__(self, name, rule):
        self.name = name
        self.rule = rule

    def predict(self, data):
        # Model with one feature: Predict a passenger survived if they are female or make with age <= 10

        predictions = []
        for _, passenger in data.iterrows():
            # Remove the 'pass' statement below
            # and write your prediction conditions here
            # print (passenger['Sex'])
            predictions.append(self.rule(passenger))
        # Return our predictions
        return pd.Series(predictions)
