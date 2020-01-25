from sklearn.metrics import fbeta_score
from sklearn.metrics import accuracy_score

def train_predict(learner, sample_size, X_train, y_train, X_test, y_test):
    '''
    inputs:
       - learner: the learning algorithm to be trained and predicted on
       - sample_size: the size of samples (number) to be drawn from training set
       - X_train: features training set
       - y_train: income training set
       - X_test: features testing set
       - y_test: income testing set
    '''

    results = {}

    # TODO: Fit the learner to the training data using slicing with 'sample_size' using .fit(training_features[:], training_labels[:])
    start = time()  # Get start time
    learner = None
    end = time()  # Get end time

    # TODO: Calculate the training time
    results['train_time'] = None

    # TODO: Get the predictions on the test set(X_test),
    #       then get predictions on the first 300 training samples(X_train) using .predict()
    start = time()  # Get start time
    predictions_test = None
    predictions_train = None
    end = time()  # Get end time

    # TODO: Calculate the total prediction time
    results['pred_time'] = None

    # TODO: Compute accuracy on the first 300 training samples which is y_train[:300]
    results['acc_train'] = None

    # TODO: Compute accuracy on test set using accuracy_score()
    results['acc_test'] = None

    # TODO: Compute F-score on the the first 300 training samples using fbeta_score()
    results['f_train'] = None

    # TODO: Compute F-score on the test set which is y_test
    results['f_test'] = None

    # Success
    print("{} trained on {} samples.".format(learner.__class__.__name__, sample_size))

    # Return the results
    return results
