from flask import Flask,render_template,request
from managers.database_manager import *


app = Flask(__name__)
app.config.from_pyfile('config.cfg')


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/postmethod', methods=['POST'])
def postmethod():
    data = request.get_json()#or get_json()?
    print(data)
    #save data to cloud database
    #add_measurement()
    return '', 201


if __name__ == '__main__':
    app.run()

