# coding: utf-8

from firebase import buscarUltimasTemperaturas
from firebase import buscarTemperaturasDoDia
from datetime import datetime


def main():
    #data = datetime(2020, 8, 24)
    resposta = buscarTemperaturasDoDia()
    #resposta = buscarUltimasTemperaturas(12)
    print(resposta)


if __name__ == '__main__':
    main()
