from flask import Flask
import json
from flask import render_template,request,jsonify
import server_files.mongo_connect as mdb
import server_files.sql_connect as sdb
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html",geo_locations=mdb.geo_locations())


@app.route('/', methods=["POST"])
def get_value():
    location=request.form['geo_location']
    database=request.form['database']
    all_data,data_heading=mdb.fetch_data_mongo(str(location))
    return render_template("index.html")

@app.route('/data_heading')
def data_heading():
    return jsonify(mdb.geo_locations())

@app.route('/all_data_mongo')
def all_data_mongo():
    location = request.args.get('data', type=str)
    a,b=mdb.fetch_data_mongo(str(location))
    return jsonify(a,b)

@app.route('/all_data_sql')
def all_data_sql():
    location = request.args.get('data', type=str)
    a,b,c=sdb.fetch_data_sql(str(location))
    return jsonify(a,b,c)

if __name__ == '__main__':
    app.run()
