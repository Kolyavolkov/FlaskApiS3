__version__ = "0.1.0"
from flask import Flask
from flask_bootstrap import Bootstrap

from restapi.filters import datetimeformat, file_type


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.secret_key = "secret"
app.jinja_env.filters["datetimeformat"] = datetimeformat
app.jinja_env.filters["file_type"] = file_type


import restapi.api
import restapi.views


if __name__ == "__main__":
    app.run(host="0.0.0.0")
