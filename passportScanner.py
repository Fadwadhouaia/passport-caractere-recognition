from passporteye import read_mrz
from datetime import datetime

#important necessary files for exposing web service
#bch nsob tkhallini nhot l path
import os
from flask import request, jsonify
from werkzeug import secure_filename

#tawa bch na9raw l image

mrz = read_mrz('samples\chiguifi.jpg')

#bch njibou les données mel passport fetch data

mrz_data = mrz.to_dict()

print('Nationality :'+ mrz_data['nationality'])
print('Date of birth :'+ mrz_data['date_of_birth'])
#datemrz = mrz_data['date_of_birth']
#print(datetime.strptime(datemrz, '%Y %m %d').date())
print('ID Number :'+ mrz_data['personal_number'])

