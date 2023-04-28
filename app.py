from flask import Flask, render_template, request

app = Flask(__name__, template_folder='static/template', static_folder='static')


@app.route('/', methods=['GET'])
def Home():
    return render_template('home.html')


@app.route('/gdp', methods=['GET'])
def get_GDP():
    return render_template('GDP.html')


@app.route('/map', methods=['GET'])
def get_AlongYear():
    return render_template('AlongYear.html')


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=80)
    app.run()
