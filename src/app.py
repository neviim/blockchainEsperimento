#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Neviim - 2018
# V-0.1.0

import hashlib
import json


class Block(object):
    """ docstring para Block.
        Aplicando o metodo hashlib:
            >> m = hashlib.sha256()
            >> m.hexdigest()
            'e570397d71e5274fe94a51b084dd47c2b4bfd61b6f76c2fdce829ffcb6d1162a'

        Uso:
                block = Block(1, "01/01/2018", {"neviim": "jads"}, "0")

                print(block.calculateHash())
                print(block.get())
    """
    def __init__(self, index, timestamp, data, previousHash=''):
        super(Block, self).__init__()
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.crypto256 = hashlib.sha256()
        self.hash = ""

    def calculaHash(self):
        """ Calcula o hash da estrutura de dados passada por parametro.

            Uso:
                block.calculaHash()
        """
        string = str(self.index) + self.previousHash + str(self.timestamp) + str(json.dumps(self.data))
        self.crypto256.update(string.encode("UTF-8"))
        self.hash = self.crypto256.hexdigest()
        return self.hash

    def get(self):
        """ Retorna estrutura block
            Calcula o hash do bloco e retorna uma estrutura json com os campos e
            o hash calculado.

                Uso:
                    block.get()
        """
        self.hash = self.calculaHash()
        gblock = { "index": self.index,
                   "previousHash": self.previousHash,
                   "timestamp": self.timestamp,
                   "data": self.data,
                   "hash": self.hash}
        return gblock


class Blockchain(object):
    """docstring para Blockchain."""
    def __init__(self):
        super(Blockchain, self).__init__()
        self.corrente = corrente


if __name__ == '__main__':
    # validando classe
    block = Block(1, "01/01/2018", {"neviim": "jads"}, "0")

    print(block.get())
