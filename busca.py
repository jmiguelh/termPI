# coding: utf-8

from firebase import buscarUltimasTemperaturas


def main():
    resposta = buscarUltimasTemperaturas(10)
    for post in resposta:
        # print(u'{} => {}'.format(post.id, post.to_dict()))
        temp = post.to_dict()
        print(temp['temperatura'])
        # print(temp['datahora'])


if __name__ == '__main__':
    main()
