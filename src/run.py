#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Neviim - 2018
# V-0.1.0

from block import Block

""" Função para gerar a blockchain
    def addBlock(bckChain, bckAtual, bckTotal ):
        # gera lista de blocos
        for i in range(0, bckTotal):
            bckNovo = bl.proximoBlock(bckAtual)
            bckChain.append(bckNovo)
            bckAtual = bckNovo
            # resultado de hash e previousHash que foram gerados ao gravar o block.
            print("Block #{} adicionado ao blockchain!".format(bckNovo.index))
            print("Hash Atual: {}".format(bckNovo.hash))
            print("Hash Prev.: {}".format(bckNovo.previousHash))
            print()
        #
        return True
"""

if __name__ == '__main__':
    # cria genesis block
    bckChain  = [Block.criaGenesisBlock()]
    bckAtual  = bckChain[0]
    bckTotal = 5

    # cria uma seguencia de (totalBlocos) na blockchain.
    # Block.addBlock(blockChain, blockAtual, totalBlocos)
    for i in range(0, bckTotal):
        bckNovo = Block.proximoBlock(bckAtual)
        bckChain.append(bckNovo)
        bckAtual = bckNovo

        # resultado de hash e previousHash que foram gerados ao gravar o block.
        print("Block #{} adicionado ao blockchain!".format(bckNovo.index))
        print("Hash Atual: {}".format(bckNovo.hash))
        print("Hash Prev.: {}".format(bckNovo.previousHash))
        print()
