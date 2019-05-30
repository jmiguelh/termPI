# coding: utf-8

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime


def conectarFirebase():
    cred = credentials.Certificate(
        'termpi-firebase-adminsdk-mfrvk-b95cdce7ef.json')
    firebase_admin.initialize_app(cred)
    return firestore.client()


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


def buscarTemperaturaAtual():
    db = conectarFirebase()
  
    temperaturas = db.collection(u'temp')
    query = temperaturas.order_by(
        u'datahora', direction=firestore.Query.DESCENDING).limit(1)
    results = query.get()
    
    return results

def buscarUltimasTemperaturas(quantidade):
    db = conectarFirebase()
  
    temperaturas = db.collection(u'temp')
    query = temperaturas.order_by(
        u'datahora', direction=firestore.Query.DESCENDING).limit(quantidade)
    results = query.get()
    
    return results
