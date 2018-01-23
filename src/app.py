#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Neviim - 2018
# V-0.2.0

# Obs: manterei as linha print() no codigo por uma questão academica e poder
#      acompanhar os resultados das variaveis por onde a execucão passar e
#      desta forma poder melhor compreender o que o algoritimo esta realizando.

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
    def __init__(self, index=0, timestamp="", data="", previousHash=""):
        super(Block, self).__init__()
        self.crypto256 = hashlib.sha256()
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculaHash()

    def calculaHash(self):
        """ Calcula o hash da estrutura de dados passada por parametro.

            Uso:
                block.calculaHash()
        """
        string = str(self.index) + self.previousHash + str(self.timestamp) + str(json.dumps(self.data))
        self.crypto256.update(string.encode("UTF-8"))
        return self.crypto256.hexdigest()

    def set(self, novoBlock):
        self.index = novoBlock.index
        self.timestamp = novoBlock.timestamp
        self.data = novoBlock.data
        self.previousHash = novoBlock.previousHash
        self.hash = novoBlock.hash
        return

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


class Blockchain(Block):
    """docstring para Blockchain."""
    def __init__(self):
        super().__init__()
        super(Blockchain, self).__init__()
        self.chain = [self.criaGenesisBlock()]

    def criaGenesisBlock(self):
        genesis = Block(0, "01/01/2017", {"bloco": "Genesis"}, "0")
        self.set(genesis)
        return genesis

    def adicionaBlock(self, novoBlock):
        novoBlock.previousHash = self.getUltimoBlock().hash
        novoBlock.hash = novoBlock.calculaHash()
        self.chain.append(novoBlock)
        self.set(novoBlock)
        return

    def getUltimoBlock(self):
        return self.chain[len(self.chain) - 1]

    def getChain(self):
        return self.chain

    def blockValido(self):
        pass 

# esta função não sera mantida.
def myDebug(chain, genesis):
    """ debug print """
    # block Genesis
    print(genesis.data)
    print(genesis.timestamp)
    print("...")

    # Corrent de bloco
    print(chain.data)
    print(chain.timestamp)
    print("...")

    # le ultimo bloco e adiciona um novo bloco
    print(chain.chain)
    print(chain.getUltimoBlock())
    print(chain.adicionaBlock())

    # adiciona um novo bloco



# inicio passo a passo a depuracao...
if __name__ == '__main__':
    # validando classe
    # block = Block(1, "01/01/2018", {"neviim": "jads"}, "0")
    # block = Block()
    # print(block.get())
    # print("...")

    # Instancia seguencia de blocos e cria bloco genesis 0
    chain = Blockchain()
    genesis = chain.criaGenesisBlock()
    print(chain.get())
    print("...")

    # adiciona bloco 1
    chain.adicionaBlock(Block(1, "23/01/2018", { "estrela": "orion", "valor": 1 }))
    print(chain.get())
    print("...")

    # adiciona bloco 2
    chain.adicionaBlock(Block(2, "23/01/2018", { "planeta": "terra", "valor": 2 }))
    print(chain.get())
    print("...")

    # imprime variaveis
    #myDebug(chain, genesis)
