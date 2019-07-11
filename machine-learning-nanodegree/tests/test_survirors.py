# Import libraries necessary for this project
from builtins import print
    
import pandas as pd

def data():
    #This option made "appearing all columns" work. Was showing fewer columns
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_rows', 10)
    pd.set_option('display.max_columns', 100)
    in_file = 'titanic_data.csv'
    full_data = pd.read_csv(in_file)

    return full_data

def outcomes(data):

    # nothing yet
    outcomes = data['Survived']
    data.drop('Survived', axis=1, inplace=True)

    return outcomes


def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """

    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred):

        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean() * 100)

    else:
        return "Number of predictions does not match number of outcomes!"


def predictions_0(data):
    """ Model with no features. Always predicts a passenger did not survive. """

    predictions = []
    for _, passenger in data.iterrows():
        # Predict the survival of 'passenger'
        predictions.append(0)

    # Return our predictions
    return pd.Series(predictions)


def predictions_1(data):
    """ Model with one feature: 
            - Predict a passenger survived if they are female. """

    predictions = []
    for _, passenger in data.iterrows():
        # Remove the 'pass' statement below
        # and write your prediction conditions here
        #print (passenger['Sex'])
        predictions.append(passenger['Sex'] == 'female')
    # Return our predictions
    return pd.Series(predictions)

def predictions_2(data):
    """ Model with one feature: 
            - Predict a passenger survived if they are female. """

    predictions = []
    for _, passenger in data.iterrows():
        # Remove the 'pass' statement below
        # and write your prediction conditions here
        #print (passenger['Sex'])
        predictions.append(passenger['Sex'] == 'female'
                           or (passenger['Sex'] == 'male' and passenger['Age'] <=10))
    # Return our predictions
    return pd.Series(predictions)


def predictions_3(data):
    """ Model with one feature: 
            - Predict a passenger survived if they are female. """

    predictions = []
    for _, passenger in data.iterrows():
        # Remove the 'pass' statement below
        # and write your prediction conditions here
        #print (passenger['Sex'])
        predictions.append(passenger['Sex'] == 'female'
                           or (passenger['Sex'] == 'male' and passenger['Age'] <=10)
                           )
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
data = data()
outcomes = outcomes(data)

# Scenario 1
#predictions = pd.Series(np.ones(5, dtype = int))
#print(accuracy_score(outcomes[:5], predictions))

# Scenario 2
#predictions = predictions_2(data)
predictions = predictions_3(data)

# Predicting how
print(accuracy_score(outcomes, predictions))
# Make the predictions
#vs.survival_stats(data, outcomes, 'Sex')