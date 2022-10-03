from flask import Flask, render_template, request, jsonify
import json
import ipinfo

app = Flask(__name__)

@app.route('/confirm', methods=['POST'])
def foo():
    file = open('/var/www/ipinfo.txt',mode='r')
    token = file.read().rstrip()
    file.close()
    handler = ipinfo.getHandler(token)

    user_agent = request.headers.get('User-Agent', None)
    real_ip = request.headers.get('X-Real-Ip', None)

    details = handler.getDetails(real_ip)

    data = request.json

    merged_dict = {**data, **details.all}
    json_merged = json.dumps(merged_dict)
    print(json_merged)
    with open('forms.json', 'w') as outfile:
        outfile.write(json_merged)

@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    print("error function")
    user_agent = request.headers.get('User-Agent', None)
    real_ip = request.headers.get('X-Real-Ip', None)
    data = request.json
    print(data)
    f = open('forms.txt', 'a')
    entry = str(real_ip) + ',' + str(json.dumps(data)) + ',' + str(user_agent) + '\n'
    return render_template('success.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=9000)
