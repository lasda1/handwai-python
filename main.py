from flask import Flask
from flask import jsonify
import controllers 
app = Flask(__name__)

@app.route('/statistic/<type>/<vendor_id>')
def get_statistic_by_vendor_id(type,vendor_id):
    if(type == "1"):
        controllers.get_statistic_for_vendor_fairs_per_hour(vendor_id)
    elif (type == "2"):
        controllers.get_statistic_for_vendor_distance_per_hour(vendor_id)
    response=jsonify(response = "true")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/distance/<vendor_id>')
def get_total_distance_morning_by_vendor_id(vendor_id):
    distance = controllers.calculate_total_distance_morning(vendor_id)
    response=jsonify(distance = distance)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/amount/<vendor_id>')
def get_total_amount_morning_by_vendor_id(vendor_id):
    amount = controllers.calculate_totals_amounts_morning(vendor_id)
    response = jsonify(amount = amount)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

