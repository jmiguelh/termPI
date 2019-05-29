# coding: utf-8

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime


def incluirTemperatura(temperatura):
    cred = credentials.Certificate(
        'termpi-firebase-adminsdk-mfrvk-b95cdce7ef.json')
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    now = datetime.datetime.now()

    data = {
        u'temperatura': float(temperatura),
        u'datahora': now,
        u'ano': now.year,
        u'mes': now.month,
        u'dia': now.day,
        u'hora': now.hour,
        u'minuto': now.minute
    }

    db.collection(u'temp').document().set(data)
    return 0
