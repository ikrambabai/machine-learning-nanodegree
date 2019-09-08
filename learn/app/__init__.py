import os
import markdown
import shelve
from flask import Flask
from flask import g
from flask_restful import Resource, Api, reqparse

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


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("learn.learn")
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


class DeviceList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())
        devices = []

        for key in keys:
            devices.append(shelf[key])

        return {'message': 'Success', 'data': devices}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('device_type', required=True)
        parser.add_argument('controller_gateway', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifier']] = args

        return {'message': 'Device registered', 'data': args}, 201


api.add_resource(DeviceList, "/learning")

