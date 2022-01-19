"""The Module is contains an endpoints API and written Flask.

    .. curent module::
        codeTest.app
"""
import logging
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
from codeTest.core import db
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__, static_url_path="")
CORS(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


SWAAGGER_URL = "/swagger"
API_URL = "/api-docs/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAAGGER_URL, API_URL,
    config={
        "app_name": "CodeTest"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAAGGER_URL)


@app.route("/")
@cross_origin()
def serveDefaultPath():
    """A Method is used for creating index file from satatic UI.

    Decorators:
        @app.route("/")
        @cross_origin

    Returns:
        static webpage.
    """
    return app.send_static_file("index.html")


@app.route("/createRecords", methods=["POST"])
@cross_origin()
def createRecords():
    """A Method is used for creating a new records sent from UI.

    Descriptions: 
        This method create new records and store it in database 
        and this API is requested from Forms.js script in client.

    Decorators:
        @app.route("/createRecords", methods=["POST"])
        @cross_origin

    Returns:
        dict, returns dictionary object with key value pairs.
    """
    db.createDatabaseTable()

    teamName = request.json.get("teamName")
    roleName = request.json.get("roleName")
    parameters = (teamName, roleName)

    result = db.getConfig(teamName=teamName, roleName=roleName)
    if not result:
        db.insertConfig(parameters)
    
    return jsonify(request.json)


@app.route("/getAllRecords", methods=["GET"])
@cross_origin()
def getAllRecords():
    """A Method is used for fetch all the data from database.

    Descriptions:
        This endpoints can be used in uri to fetch the data.

    Usage:
        http://localhost:5000/getAllRecords

    Decorators:
        @app.route("/getAllRecords", methods=["GET"])
        @cross_origin

    Returns:
        returns a dictionary object with key value pairs.
    """
    db.createDatabaseTable()
    result = db.getConfig()
    if not result:
        return jsonify(
            {
                "title": (
                    "No data found in the database, " 
                    "refresh the page!."
                )
            }
        )

    records = dict()
    for _, teamName, roleName in result:
        records.setdefault(teamName, []).append(roleName)
    
    return jsonify(records)


@app.route("/getRoleNamesByTeamName", methods=["GET"])
@cross_origin()
def getRoleNamesByTeamName():
    """A Method is used for fetch the roleName by using teamName as a
    Input in url.

    Descriptions:
        This endpoints can be used in web url.

    Usage:
        http://localhost:5000/getRoleNamesByTeamName?teamName=DevOpsTeam

    Decorators:
        @app.route("/getRoleNamesByTeamName, methods=["GET"])
        @cross_origin

    Returns:
        dict, return s dictionary object with key value pairs.
    """
    args = request.args
    db.createDatabaseTable()
    result = db.getConfig(teamName=args.get("teamName"))

    if not result:
        return jsonify(
            {
                "title": "No data found in the database, refresh the page!."
            }
        )
    
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)