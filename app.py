from flask import Flask, render_template, send_file, request

app = Flask(__name__, template_folder='static/template', static_folder='static')


@app.route('/', methods=['GET'])
def Home():
    return send_file('static/template/index.html')


@app.route('/GDP', methods=['GET'])
def get_GDP():
    return render_template('GDP.html')


@app.route('/AlongYear', methods=['GET'])
def get_AlongYear():
    year = request.args.get('year')
    return render_template('AlongYear.html', year=year)


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=80)
    app.run(port=8080)
