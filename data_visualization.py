from flask import Flask, render_template
import plotly
import plotly.graph_objs as go
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://10.254.2.50:5001/data')
    data = response.json()

    graphs = []

    for server, metrics in data.items():
        times = [entry['time'] for entry in metrics]
        cpu_usages = [entry['cpu'] for entry in metrics]
        ram_usages = [entry['ram'] for entry in metrics]

        graphs.append(
            go.Scatter(x=times, y=cpu_usages, mode='lines', name=f'{server} CPU')
        )
        graphs.append(
            go.Scatter(x=times, y=ram_usages, mode='lines', name=f'{server} RAM')
        )

    graph_json = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graph_json=graph_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
