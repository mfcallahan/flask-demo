from flask import Flask, Blueprint, jsonify
import arcpy
import arcgis

app = Flask(__name__)

# Define a Flask Blueprint to set the root url of the app to http://localhost:5000/flask-demo
APP_PREFIX = "flask-demo"
appBlueprint = Blueprint(
    APP_PREFIX,
    __name__,
    url_prefix=f"/{APP_PREFIX}"
)

@appBlueprint.route("/hello", methods=["GET"])
def hello():
    response = {
        "message": f"Hello! This app is powered by Python + Flask."
    }

    return jsonify(response)

@appBlueprint.route("/checkArcPy", methods=["GET"])
def checkArcPy():
    try:
        ver = arcpy.GetInstallInfo()["Version"]
    except:
        response = {
            "message": "arcpy.GetInstallInfo() failed."
        }

        return jsonify(response)
        
    response = {
        "message": f'arcpy.GetInstallInfo()["Version"] output: {ver}'
    }

    return jsonify(response)

@appBlueprint.route("/checkArcGISPythonAPI", methods=["GET"])
def checkArcGISPythonAPI():
    try:
        ver = arcgis.__version__
    except:
        response = {
            "message": "arcgis.__version__ failed."
        }

        return jsonify(response)
        
    response = {
        "message": f"arcgis.__version__ output: {ver}"
    }

    return jsonify(response)

# Register the blueprint with the Flask app
app.register_blueprint(appBlueprint)

if __name__ == "__main__":
    app.run()
