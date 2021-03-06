# coding: utf-8

import configparser
from firebase import incluirTemperatura

pi = False


def lerConfig():
    config = configparser.ConfigParser()
    config.read_file(open('config.ini'))
    if pi:
        arquivo = config['PI']['path']
    else:
        arquivo = config['DEV']['path']
    arquivo = arquivo + config['DEVICE']['termometro'] + \
        '/' + config['DEVICE']['arquivo']
    return arquivo


def retornaTemperatura():
    file = lerConfig()
    arquivo = open(file, 'r')
    for linha in arquivo:
        posicao = linha.find('t=')
        if posicao > 0:
            temperatura = int(linha[posicao+2:])/1000
    arquivo.close()
    return temperatura


def main():
    temperatura = retornaTemperatura()
    temperatura = retornaTemperatura()
    if pi:
        incluirTemperatura(temperatura)
    else:
        print(temperatura)


if __name__ == '__main__':
    main()
