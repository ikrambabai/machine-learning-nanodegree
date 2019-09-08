from learn.project1.services import load_data
from learn.project1.services import separate_truth_from_data
from learn.project1.models.predictor import Predictor

""" load data """
data = load_data()
truth, data = separate_truth_from_data(data)

""" scenario1 """
predictor = Predictor('Top five in loaded file survived', lambda ps: 1)
predictor.predict(data[:5])
predictor.accuracy_score(truth[:5])

""" scenario2 """
predictor = Predictor('Sex = female', lambda ps: ps['Sex'] == 'female')
predictor.predict(data)
predictor.accuracy_score(truth)

""" scenario3 """
predictor = Predictor('Sex = female or male but with age <=10',
                      lambda ps: ps['Sex'] == 'female' or (ps['Sex'] == 'male' and ps['Age'] <= 10))
predictor.predict(data)
predictor.accuracy_score(truth)

