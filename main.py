from flask import Flask
# import db
import myproject1
app = Flask(__name__)



@app.route("/yanshul")
def index_data():
    return myproject1.index_data()

@app.route("/hello")
def index_daa():
    return "YYYY"
if __name__ == '__main__':
    app.run()
# You can then add the endpoint http://localhost:5000/ to Postman to test the API.




