#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Neviim - 2018
# V-0.3.0

# Obs: Este estudo tem a finalidade de entender o funcionamento de uma estrutura
#      de bloco com os seus detalhes procedurais de funcionamento.
#      Este codigo é a otimização apos a compreenção do codigo da versão 0.2.0,
#      aplicando algumas otimizações e melhorias estruturais.

""" Aplicando o metodo hashlib:

        >>> m = hasher.sha256()
        >>> m.hexdigest()
        'e570397d71e5274fe94a51b084dd47c2b4bfd61b6f76c2fdce829ffcb6d1162a'
"""

import hashlib as hasher
import datetime as date
import json

#
class Block():
    """ Docstring para Block.
        Para cada bloco a ser armazenado, coloca um timestamp e um índice.

        Uso:
            from block import Block as bl

            blockchain  = [bl.criaGenesisBlock()]
            blockAtual  = blockchain[0]
    """
    def __init__(self, index, timestamp, data, previousHash):
        super(Block, self).__init__()
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculaHashBlock()

    def calculaHashBlock(self):
        """ Calcula o hash da estrutura de dados recebida por parametro.
            Cada cadeia de bloco terá um hash auto-identificavel.

            Uso:
                block.calculaHashBlock()

            Retorna:
                Hash codificado.
        """
        lStrBloco = (str(self.index).encode('utf-8') +
                     str(self.timestamp).encode('utf-8') +
                     str(self.data).encode('utf-8') +
                     str(self.previousHash).encode('utf-8'))
        #
        lsha = hasher.sha256()
        lsha.update(lStrBloco)
        return lsha.hexdigest()

    def criaGenesisBlock():
        """ Cria o bloco genesis
        """
        return Block(0, date.datetime.now(), {"nome": "bloco genesis"}, "0")

    def proximoBlock(aBlock):
        """ Consolida os dados do bloco a ser gerado, retornando no novo bloco
            os seus respectivos dados.
        """
        lindex = aBlock.index + 1
        ltimestamp = date.datetime.now()
        ldata = str({"nome": "Block Neviim Jads"}) + str(lindex)
        lhash = aBlock.hash
        return Block(lindex, ltimestamp, ldata, lhash)
