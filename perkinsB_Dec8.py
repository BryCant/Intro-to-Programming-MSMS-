from flask import Flask
from datetime import datetime
import os

os.system('cls')

app = Flask(__name__)


@app.route('/')
def hello():
    return """<html><body>
    The time is """ + str(datetime.now()) + """.
    <h1>Hello, world!</h1>
    </body></html>"""


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)
