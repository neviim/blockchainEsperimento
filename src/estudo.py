#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Neviim - 2018
# V-0.2.0

# Obs: manterei as linha print() no codigo por uma questão academica e poder
#      acompanhar os resultados das variaveis por onde a execucão passar e
#      desta forma poder melhor compreender o que o algoritimo esta realizando.

import hashlib
import json


class Block():
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
        self.hash = ""

    def calculaHash(self):
        """ Calcula o hash da estrutura de dados passada por parametro.

            Uso:
                block.calculaHash()
        """
        string = str(self.index) + self.previousHash + str(self.timestamp) + str(json.dumps(self.data))
        self.crypto256.update(string.encode("UTF-8"))

        print("")
        print("def calculaHash(self)")
        print("String.......................: ", string)
        print("Hash SHA256..................: ", self.crypto256.hexdigest())
        print("...")

        self.hash = self.crypto256.hexdigest()
        return self.hash

    def setBlock(self, novoBlock):
        self.index = novoBlock.index
        self.timestamp = novoBlock.timestamp
        self.data = novoBlock.data
        self.previousHash = novoBlock.previousHash
        self.hash = novoBlock.hash
        return

    def getBlock(self, gblock):
        gblock = { "index": gblock.index,
                   "previousHash": gblock.previousHash,
                   "timestamp": gblock.timestamp,
                   "data": gblock.data,
                   "hash": gblock.hash}
        return gblock

    def get(self):
        """ Retorna estrutura block
            Calcula o hash do bloco e retorna uma estrutura json com os campos e
            o hash calculado.

                Uso:
                    block.get()
        """
        #self.hash = self.calculaHash()
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
        self.chain = []
        self.criaGenesisBlock()

    def criaGenesisBlock(self):
        genesis = Block(0, "01/01/2017", {"bloco": "Genesis"}, "0")
        genesis.hash = self.calculaHash()
        self.chain = [genesis]
        self.setBlock(genesis)

        print("")
        print(">>> ", self.getBlock(genesis))

        #
        print("")
        print("def criaGenesisBlock(self)")
        print("block genesis................: ", genesis)
        print("Hash do block genesis........: ", genesis.hash)
        print("PreviusHash do bloco genesis.: ", genesis.previousHash)
        print("self.get.....................: ", self.get())
        print("...")
        #
        return genesis

    def adicionaBlock(self, novoBlock):
        novoBlock.previousHash = self.getUltimoBlock().hash
        novoBlock.hash = novoBlock.calculaHash()
        #
        print("")
        print("def adicionaBlock(self, novoBlock)")
        print("Matrix blocos................: ", self.chain)
        print("...")

        print("Hash do Bloco anterior.......: ", self.getUltimoBlock().hash)
        print("Hash do Bloco atual..........: ", novoBlock.hash)
        print("...")
        #
        self.chain.append(novoBlock)
        self.setBlock(novoBlock)
        return

    def getUltimoBlock(self):
        utimoBlock = self.chain[len(self.chain) - 1]
        print("")
        print("def getUltimoBlock(self)")
        print("Ultimo bloco.................: ", utimoBlock)
        print("...")
        return utimoBlock

    def getChain(self):
        return self.chain

    def blockValido(self):
        for reg in range(1, len(self.getChain())):
            blockAtual = self.chain[reg]
            blockAnterior = self.chain[reg - 1]

            print()
            print("reg      >>> ", reg)
            print("Atual    >>> ", blockAtual)
            print("Anterior >>> ", blockAnterior)

            #
            print()
            print("def blockValido(self)")
            print("Matrix blocos................: ", self.chain)
            print()
            print("bloco atual..................: ", blockAtual)
            print("Hash do bloco atual..........: ", blockAtual.hash)
            print("bloco anterior...............: ", blockAnterior)
            print("Hash do bloco anterior.......: ", blockAnterior.hash)
            print("...")

            print("bloco atual calcula hash.....: ", blockAtual.calculaHash())
            print("...")
            #

            hashAtual = blockAtual.hash
            hashCalculado =  blockAtual.calculaHash()
            #self.setBlock()

            print()
            print("Hash atual e Hash recalculado")
            print("Block ............      >>> ", blockAtual)
            print("Hash atual arquivo      >>> ", hashAtual)
            print("Hash atual recalculado  >>> ", hashCalculado)
            print("Todos os itens do bloco >>> ", self.getBlock(blockAtual))
            #

            if (blockAtual.hash != blockAtual.calculaHash()):
                return False
            #if (blockAtual.previousHash != blockAnterior.hash):
            #    return False

        return True


# inicio passo a passo a depuracao...
if __name__ == '__main__':
    # Instancia seguencia de blocos e cria bloco genesis 0
    blockchain = Blockchain()

    # adiciona bloco 1
    print("")
    print("###")
    print("Adiciona um block 1")
    print("-------------------")
    blockchain.adicionaBlock(Block(1, "23/01/2018", { "estrela": "orion", "valor": 1 }))

    print("")
    print("***")
    print(blockchain.get())
    print("...")

    # adiciona bloco 2
    print("")
    print("###")
    print("Adiciona um block 2")
    print("-------------------")
    blockchain.adicionaBlock(Block(2, "23/01/2018", { "planeta": "terra", "valor": 2 }))
    print(blockchain.get())
    print("...")

    # valida blocos
    print("")
    print("###")
    print("Valida os blocos")
    print("-------------------")
    print("Bloco valido? ", blockchain.blockValido())
