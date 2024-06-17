from flask import render_template, jsonify, request
from flask_app import app

from flask_app.utils import perform_speedtest

@app.route("/helloworld")
def helloworld():
    return "Hello World ;)"

@app.route("/")
def index():
    user_ip, user_isp = perform_speedtest.get_client_info()
    server_name, server_isp = perform_speedtest.get_server_info()
    user_info = {'ip': user_ip, 'isp': user_isp}
    server_info = {'name': server_name, 'isp': server_isp}
    return render_template("index.html", user=user_info, server=server_info)

@app.route("/start-speedtest", methods=['GET'])
def start_speedtest():
    user_ip = request.args.get('userIP')
    results = perform_speedtest.start_speed(user_ip)
    return jsonify(results)

@app.route("/convert-mbps-to-MBps", methods=['POST'])
def convert_results():
    results = request.json
    new_results = perform_speedtest.convert_speedtest_results(results)
    return jsonify(new_results)