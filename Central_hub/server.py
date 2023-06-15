# Import the Flask and jsonify classes from the flask module
from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from store import dashboardData, nodeData


def check_values():
    global heading, sensor1, sensor2
    heading = dashboardData()
    sensor1 = nodeData('node1.csv')
    sensor2 = nodeData('node2.csv') 

def create_App():
    global heading, sensor1, sensor2
    app = Flask(__name__)

    @app.route('/dashboard')
    def get_dashboard_data():
        # Create a List containing the Node # and recent data
        data = heading
        return jsonify(data=data)

    @app.route('/sensor1')
    def get_sensor1_data():
        data = sensor1
        # Return a JSON response with the data list
        return jsonify(data=data)

    @app.route('/sensor2')
    def get_sensor2_data():
        data = sensor2
        # Return a JSON response with the data list
        return jsonify(data=data)

    # Start the APScheduler to run check_values() every minute
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_values, 'interval', minutes=1)
    scheduler.start()

    app.run(host='0.0.0.0', port=5000)
