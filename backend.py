# This Python file uses the following encoding: utf-8

import sqlite3 as conector
import json
import urllib.request
import re

def lambda_handler(event):
    try:
        return json.loads(urllib.request.urlopen(_get_url_api(event)).read())
    # return json.loads(urllib.request.urlopen(_get_url_api(event['cep'])).read())
    except:
        return json.loads("{\"erro\": true, \"mensagem\": \"Formato incorreto\"}")

def _get_url_api(cep):
    return ('http://www.viacep.com.br/ws/{}/json'.format(_replace(cep)))

def _replace(str):
    return str.replace("-", "").replace(" ", "")

def _regex(str):
    return re.match('[0-9]{8}', _replace(str))

def getInfoByCep(cep):
    d = lambda_handler(cep)
    dd = {'cep': d['cep'],
        'logradouro': d['logradouro'],
        'complemento': d['complemento'],
        'bairro': d['bairro'],
        'localidade': d['localidade'],
        'uf': d['uf'],
        'ddd': d['ddd']}
    return dd

##################################################3333

def cityData():
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()
    ## N SEI MODELAGEM DE BD
    ### ESSE É O MELHOR Q POSSO FAZER
    comando = '''CREATE TABLE IF NOT EXISTS Cidade(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     cep INTEGER NOT NULL,
                     logradouro TEXT NOT NULL,
                     complemento TEXT,
                     bairro TEXT NOT NULL,
                     localidade TEXT NOT NULL,
                     uf CHARACTER(2) NOT NULL,
                     ddd INTEGER NOT NULL
                     );'''
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()


def addCityRec(cep, logradouro, complemento, bairro, localidade, uf, ddd):
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()
    comando = ''' INSERT INTO Cidade VALUES(NULL, ?, ?, ?, ?, ?, ?, ?);'''
    cursor.execute(comando, (cep, logradouro, complemento, bairro, localidade, uf, ddd))
    conexao.commit()
    cursor.close()
    conexao.close()

def viewDate():
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Cidade")
    rows = cursor.fetchall()
    cursor.close()
    conexao.close()
    return rows

def deleteRec():
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Cidade WHERE id=?", (id))
    conexao.commit()
    cursor.close()
    conexao.close()

def searchData(cep="", logradouro="", complemento="", bairro="", localidade="", uf="", ddd=""):
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECTE * FROM Cidade WHERE cep=? OR logradouro=? OR complemento=? OR bairro=? OR localidade=? OR uf=? OR ddd=?", cep, logradouro, complemento, bairro, localidade, uf, ddd)
    rows = cursor.fetchall()
    cursor.close()
    conexao.close()
    return rows

def updateData(id, cep="", logradouro="", complemento="", bairro="", localidade="", uf="", ddd=""):
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE Cidade SET cep=? OR logradouro=? OR complemento=? OR bairro=? OR localidade=? OR uf=? OR ddd=? WHERE id=?", cep, logradouro, complemento, bairro, localidade, uf, ddd, id)
    conexao.commit()
    cursor.close()
    conexao.close()


def getcep(v):
    print(v)

