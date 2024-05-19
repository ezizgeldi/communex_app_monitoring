from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/metrics', methods=['GET'])
def get_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    return jsonify(cpu=cpu_usage, ram=ram_usage)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

