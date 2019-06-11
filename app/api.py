#Import required dependencies
from flask import Flask, jsonify, abort, make_response, request
from bson.json_util import dumps
import requests
import json
import uuid
import os
import pyfiglet
import re

conUri = os.getenv("data_api", "http://umc-api.maartenmol.nl:5000")

#Print some usefull information to console
ascii_banner = pyfiglet.figlet_format("UMC Voice-API")
print(ascii_banner)
print("Starting API Server")
print("API Server Version: V1.0")
print("Developed by: Haydn Felida, Jeroen Verkerk, Sam Zandee, Shaniah Arrias, Maarten Mol. (All rights reserved)")

#Define Word Types for Split
def getWords():
    typeWords = ['temperatuur', 'bloeddruk', 'gewicht']
    return typeWords

#Define app with Flask
app = Flask(__name__)

#Define error function for JSON error response
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "notFound"}), 404)

#Define the root
@app.route("/")
def index():
    return "Please use the V1 API! Developed by: Haydn Felida, Jeroen Verkerk, Sam Zandee, Shaniah Arrias, Maarten Mol. (All rights reserved)"

#Define PROCESS VOICE DATA
@app.route('/api/v1/voice/', methods=['POST'])
def process_voice():
    try:
        data = json.loads(request.data)
        metric_id = data['metric_id']
        patient_id = data['patient_id']
        nurse_id = data['nurse_id']
        raw_text = data['raw_text']
        uid = uuid.uuid4().hex

        type_word = getWords()
        split_line = raw_text.split()

        # FOR TESTING
        textFilter = raw_text.lower()

        if "bloeddruk" in textFilter:
            metricState = "bloeddruk"

            metricValueRaw = re.findall('\d+', textFilter)

            metricValue = metricValueRaw[0] + "/" + metricValueRaw[1]

        if "gewicht" in textFilter:
            metricState = "gewicht"

            metricValue = int(re.search(r'\d+', textFilter).group())

        if "temperatuur" in textFilter:
            metricState = "temperatuur"

            metricValue = int(re.search(r'\d+', textFilter).group())

        # END TESTING

        for i in range(len(split_line)):
            word = split_line[i]
            if word in type_word:
                if word == "bloeddruk":
                    value = split_line[i + 2] + "/" + split_line[i + 4]
                else:
                    value = (split_line[i + 2])

                metric_type = word

        print("[DEBUG] Voice Data Processed: " + metric_type + " = " + value)

        print("##### TEST DATA INCOMMING! #####")
        print("[TESTING DEBUG] Voice Data Processed: " + metricState + " = " + metricValue)
        print("##### END OF TEST DATA! #####")

        #Data to be sent to API 
        datax = {metric_type : value}
        data = json.dumps(datax, sort_keys=True, indent=4)

        print("[DEBUG] JSON Data Generated: " + data)

        API_ENDPOINT = conUri + "/api/v1/metric/id=" + metric_id

        r = requests.put(url = API_ENDPOINT, data = data) 

        response = json.loads(r.text)

        return jsonify({"processedData":metric_type + "=" + value, "postData" : response}), 201, {'Content-Type': 'application/json; charset=utf-8'}

    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define main APP
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000", debug=True)