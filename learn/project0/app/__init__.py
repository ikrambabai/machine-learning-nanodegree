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

        """ scenario1 """
        predictor = Predictor('Top five in loaded file survived', lambda ps: 1)
        predictor.predict(data[:5])
        scenario1 = predictor.accuracy_score(truth[:5])

        """ scenario2 """
        predictor = Predictor('Sex = female', lambda ps: ps['Sex'] == 'female')
        predictor.predict(data)
        scenario2 = predictor.accuracy_score(truth)

        """ scenario3 """
        predictor = Predictor('Sex = female or male but with age <=10',
                              lambda ps: ps['Sex'] == 'female' or (ps['Sex'] == 'male' and ps['Age'] <= 10))
        predictor.predict(data)
        scenario3 = predictor.accuracy_score(truth)

        """ scenario3 (Question1) """
        predictor = Predictor('None Survived', lambda ps: 0)
        predictor.predict(data)
        scenario4 = predictor.accuracy_score(truth)

        all_scenarios = [scenario1, scenario2, scenario3, scenario4]

        return {'message': 'Success', 'data': all_scenarios}, 200


api.add_resource(PredictionList, "/learning")

