# Portugiesisches Wörterbuch #

print('Wort eingeben...')
word = input()

dictionary_de_pt = {
    "Baum": "(a) árvore",
    "essen": "comer",
    "schlafen": "dormir",
    "Sonne": "(o) sol",
    "trinken": "beber"
}

dictionary_pt_de = {
    "(a) árvore": "Baum",
    "beber": "trinken",
    "comer": "essen",
    "dormir": "schlafen",
    "(o) sol": "Sonne",
}

if word in dictionary_de_pt:
    print(dictionary_de_pt[word])
elif word in dictionary_pt_de:
    print(dictionary_pt_de[word])
else:
    print('Das Wort existiert noch nicht im Wörterbuch.')