from Trie import Trie
import unidecode
import itertools
import re


def printwachkayen(dico, word):
    a = list(word)
    for i in range(len(a)):
        temp = tuple(itertools.permutations(a, i + 1))
        for tup in temp:
            permutation = ''.join(re.findall("[a-z]+", str(tup)))
            if dico.eskefiha(permutation):
                print(permutation)


trie = Trie()

#esrot all the words
with open('francais.txt') as fp:
    for line in fp:
        if len(line) > 3:
            trie.esrot(unidecode.unidecode(line.rstrip()).lower())


while True:
    printwachkayen(trie, input("VITE, RENTRE TES LETTRES :  "))



