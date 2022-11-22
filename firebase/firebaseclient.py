import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import time
import random
from datetime import datetime

#applications deafault credentials are automatically created 
cred = credentials.Certificate('credentials.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()


while(True):
    current_date = datetime.now()
    date = current_date.strftime('%Y-%m-%d')
    hour = current_date.strftime('%H')

    collection_name = u'sensor_1_{0}'.format(date)

    hour_ref = db.collection(collection_name).document(hour)
    encendido = bool(random.getrandbits(1))

    hour_doc = hour_ref.get()
    hour_data = hour_doc.to_dict()

    totals_ref = db.collection(collection_name).document('totals')
    totals_doc = totals_ref.get()
    totals_data = totals_doc.to_dict()

    if totals_data == None:
        totals_ref.set({
            u'total_minutos_encendido' : 1 if encendido else 0,
        })
    else:
        if encendido:
            totals_ref.update({
                u'total_minutos_encendido' : totals_data[u'total_minutos_encendido'] + 1
        })
    if hour_data == None:
        hour_ref.set({
            u'encendido' : 1 if encendido else 0,
            u'apagado' : 1 if not encendido else 0,
        })
    else:
        if encendido:
            hour_ref.update({
                u'encendido' : hour_data[u'encendido'] + 1
            })
        else:
            hour_ref.update({
                u'apagado' : hour_data[u'apagado'] + 1
            })
    time.sleep(10)