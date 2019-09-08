import os
import markdown
from flask import Flask
from flask_restful import Resource, Api, reqparse
from learn.project0.services import load_data
from learn.project0.services import separate_truth_from_data
from learn.project0.models.predictor import Predictor

# Create an instance of Flask application
app = Flask(__name__)

# Create the API
api = Api(app)

# The index-endpoint (/) of the application will read the README.md file and render on the page
@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + "/README.md", 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


class PredictionList(Resource):
    def get(self):
        """ load data """
        data = load_data()
        truth, data = separate_truth_from_data(data)
        all_scenarios = []

        """ Question 1: What are the chances none survived? """
        predictor = Predictor('Question 1: What are the chances none survived?', lambda ps: 0)
        predictor.predict(data)
        scenario = predictor.accuracy_score(truth)
        all_scenarios.append(scenario)

        """ Question2: Accuracy that only females survived? """
        predictor = Predictor('Question 2: Accuracy that only females survived?', lambda ps: ps['Sex'] == 'Female')
        predictor.predict(data)
        scenario = predictor.accuracy_score(truth)
        all_scenarios.append(scenario)

        """ Question3: Accuracy that all female passengers and male under the age 10 survived? """
        predictor = Predictor('Question 3: Accuracy that all female passengers and male under the age 10 survived?',
                              lambda ps: (ps['Sex'] == 'female' or (ps['Sex'] == 'male' and ps['Age'] <= 10)))

        predictor.predict(data)
        scenario = predictor.accuracy_score(truth)
        all_scenarios.append(scenario)

        """ Question4: Accuracy that all female passengers and male under the age 10 survived? """
        predictor = Predictor('Question 4: What rule can get us a survival accuracy of 80 or more?',
                              lambda ps: (
                                             (ps['Sex'] == 'female' and ps['Pclass'] != 3)
                                             or (ps['Sex'] == 'female' and ps['Pclass'] == 3 and (ps['Parch'] == 0 or ps['Parch'] == 1))
                                             or (ps['Sex'] == 'male' and ps['Age'] <= 10)
                              ),
                              steps="The steps I followed to get > 80% accuracy were either of the three rules as "
                                    "follows (after looking at data in spreadsheet and the vs module iPython notebook)"
                                    " a). Either all females that weren't in class 3"
                                    " b). Or, all females in class 3, but with none or just 1 parent."
                                    " c). Or any male with the age less than or equal to 10.")

        predictor.predict(data)
        scenario = predictor.accuracy_score(truth)
        all_scenarios.append(scenario)

        return {'project0-questions': all_scenarios}, 200


api.add_resource(PredictionList, "/project0")

