from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)

@app.route('/confirm.html', methods=['POST'])
def foo():
    user_agent = request.headers.get('User-Agent', None)
    real_ip = request.headers.get('X-Real-Ip', None)
    data = request.json
    print(data)
    entry = str(real_ip) + ',' + str(json.dumps(data)) + ',' + str(user_agent) + '\n'
    f = open('forms.txt', 'a')
    f.write(entry)
    return render_template('success.html')
    f.close()


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