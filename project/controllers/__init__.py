import os
import requests
import json
from flask import jsonify, render_template
from project import app

@app.route('/')
def start():
    results = data()
    
    return render_template('index.html', results = results)

@app.route('/api')
def api():
    results = data()
    return jsonify(results = results)

def data():
    data = []
    proxies = []

    filename = os.path.join(app.static_folder, 'data', 'url.json')
    with open(filename) as json_file:
        urls = json.load(json_file)
        
    for url in urls:
        #if 'proxy' in url:
        #    proxies = {'http' : url['proxy'], 'https': url['proxy']}
        r = requests.get(url['url'], proxies=proxies)
        data.append({
            'url': r.url, 
            'code': r.status_code, 
            'elapsed': r.elapsed.total_seconds()
        })

    return data
