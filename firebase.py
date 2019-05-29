# coding: utf-8

from google.cloud import firestore
import google.cloud.exceptions
import datetime


def conectarFirebase():
    from google.cloud import firestore
    db = firestore.Client()
    return db


def incluirTemperatura(temperatura):
    db = conectarFirebase()
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
