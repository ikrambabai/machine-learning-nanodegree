import os
import markdown
from flask import Flask

# Create an instance of Flask application
app = Flask(__name__)


@app.route("/")
def all_learning():
    with open(os.path.dirname(app.root_path) + "/README.md", 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)






