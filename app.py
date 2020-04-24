from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/interface',methods=['POST', 'GET'])
def index():
    return render_template('interface.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
