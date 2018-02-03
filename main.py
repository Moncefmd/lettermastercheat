from Trie import Trie
import unidecode
import itertools
import re


def print_existant_subwords(dico, word):
    a = list(word)
    for i in range(len(a)):
        #Generating different sizes of permutations
        temp = tuple(itertools.permutations(a, i + 1))
        for tup in temp:
            #Getting rid of accents
            permutation = ''.join(re.findall("[a-z]+", str(tup)))
            if dico.contains(permutation):
                print(permutation)


trie = Trie()

#Populate the prefix tree with the dictionary words
with open('francais.txt') as fp:
    for line in fp:
        #Words less than three characters are not considered
        if len(line) > 3:
            trie.add_string(unidecode.unidecode(line.rstrip()).lower())


while True:
    print_existant_subwords(trie, input("VITE, RENTRE TES LETTRES :  "))



