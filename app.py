from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/sensor-data', methods=['POST'])
def receive_sensor_data():
    if request.method == 'POST':

        request_data = request.get_json()

        sensor_data = {"dados recebidos": request_data}

        return jsonify(sensor_data)


if __name__ == '__main__':
    app.run(debug=True)
