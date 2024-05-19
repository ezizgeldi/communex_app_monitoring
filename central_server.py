from flask import Flask, jsonify
import requests
import threading
import time
from datetime import datetime
app = Flask(__name__)

# Список удаленных серверов
servers = [
    'http://10.254.2.50:5000/metrics',
    'http://10.254.2.52:5000/metrics',
    #'http://server3:5000/metrics'
]

# Словарь для хранения метрик
metrics_data = {server: [] for server in servers}

def fetch_metrics():
    while True:
        for server in servers:
            try:
                response = requests.get(server)
                if response.status_code == 200:
                    data = response.json()
                    metrics_data[server].append({
                        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'cpu': data['cpu'],
                        'ram': data['ram']
                    })
            except requests.RequestException as e:
                print(f"Error fetching data from {server}: {e}")
        time.sleep(60)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(metrics_data)

if __name__ == '__main__':
    threading.Thread(target=fetch_metrics).start()
    app.run(host='0.0.0.0', port=5001)
