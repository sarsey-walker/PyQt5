# This Python file uses the following encoding: utf-8

import sqlite3 as conector
import json
import urllib.request
import re

################## FUNÇÕES PARA USO DA API "VIA CEP"  #######################3


def lambda_handler(event):
    r = json.loads(urllib.request.urlopen(_get_url_api(event)).read())
    if len(r) < 2:
        return str(r)
    else:
        return r

def _get_url_api(cep):
    return ('http://www.viacep.com.br/ws/{}/json'.format(_replace(cep)))

def _replace(str):
    return str.replace("-", "").replace(" ", "")

def _regex(str):
    return re.match('[0-9]{8}', _replace(str))

def getInfoByCep(cep):
    d = cep
    dd = {'cep': d['cep'],
        'logradouro': d['logradouro'],
        'complemento': d['complemento'],
        'bairro': d['bairro'],
        'localidade': d['localidade'],
        'uf': d['uf'],
        'ddd': d['ddd']}
    return dd

#################  FUNÇÕES PARA MANIPULAÇÃO DO BANCO DE DADOS  ###########################

def cityData():
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()
    comando = '''CREATE TABLE IF NOT EXISTS Cidade(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     cep INTEGER NOT NULL,
                     logradouro TEXT NOT NULL,
                     complemento TEXT,
                     bairro TEXT NOT NULL,
                     localidade TEXT NOT NULL,
                     aluguel INTEGER NOT NULL,
                     cd_casa INTEGER NOT NULL,
                     dono TEXT NOT NULL,
                     uf CHARACTER(2) NOT NULL,
                     ddd INTEGER NOT NULL
                     );'''
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()


def addCityRec(cep, logradouro, complemento, bairro, localidade, aluguel,cd_casa, dono,uf, ddd):
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()
    comando = ''' INSERT INTO Cidade VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''
    cursor.execute(comando, (cep, logradouro, complemento, bairro, localidade, aluguel, cd_casa, dono,  uf, ddd))
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

def knowId():
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM Cidade")
    rows = cursor.fetchall()
    cursor.close()
    conexao.close()
    return rows


def deleteRec(id):
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Cidade WHERE id=?", str(id))
    conexao.commit()
    cursor.close()
    conexao.close()

def searchData(cep="", logradouro="", complemento="", bairro="", localidade="", aluguel="",cd_casa="", dono="", uf="", ddd=""):
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECTE * FROM Cidade WHERE cep=? OR logradouro=? OR complemento=? OR bairro=? OR localidade=? OR aluguel=? OR cd_casa=? OR dono=? OR uf=? OR ddd=?", cep, logradouro, complemento, bairro, localidade, uf, ddd)
    rows = cursor.fetchall()
    cursor.close()
    conexao.close()
    return rows

def updateData(id, cep="", logradouro="", complemento="", bairro="", localidade="", aluguel="",cd_casa="", dono="", uf="", ddd=""):
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE Cidade SET cep=? OR logradouro=? OR complemento=? OR bairro=? OR localidade=? OR aluguel=? OR cd_casa=? OR dono=? OR uf=? OR ddd=? WHERE id=?", cep, logradouro, complemento, bairro, localidade, uf, ddd, id)
    conexao.commit()
    cursor.close()
    conexao.close()



