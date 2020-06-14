import os

from flask import request, jsonify, Flask
import flask
from werkzeug.utils import secure_filename
from passporteye import read_mrz

#initialiser notre serveur web
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "My passport Api running on port 2700"

#bch na3mlou methode scan
@app.route("/scan", methods=["POST"])
def scan():
    if flask.request.method=="POST":
        name_args = request.args.get('name')
        cin_args = request.args.get('cin')
        nationality_args = request.args.get('nationality')
        f = request.files["file"]
        #securizina name
        f_name = secure_filename(f.filename)
        #tawa bch nsajlouh
        f.save(f_name)
        image = read_mrz(f_name)
        imagedata = image.to_dict()
        name_passport = imagedata['surname']
        nationality_passport = imagedata['nationality']
        cin_passport = imagedata['personal_number']
        if (name_args in name_passport ) or (nationality_passport in nationality_args ) or (cin_args in cin_passport) :
            res = 'successfuly identified:' + name_passport + ' ' + nationality_passport + ' ' + cin_passport
            return jsonify(res)
        else:
            return jsonify("wrong matching")

if __name__ == "__main__":
    app.run(port=2700, debug=True)



