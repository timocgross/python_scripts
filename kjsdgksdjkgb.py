def conjugate(word, person):

    # extract the suffix for the word
    # suffix = word[-3:]

    vowels = 'aeıioöuü'

    # get the beginning of the word, without the suffix
    stem = word[:-3]
    last_letter = stem[-1]

    last_vowel = ''

    for letter in stem[::-1]:
        if (letter in vowels):
            last_vowel = letter
            break

    firstSg = {'a': 'ıyorum',
                'ı': 'ıyorum',
                'o': 'uyorum',
                'u': 'uyorum',
                'e': 'iyorum',
                'i': 'iyorum',
                'ö': 'üyorum',
                'ü': 'üyorum'}
    
    dict = {'1sg': firstSg}

    if (last_vowel == ''):
        return stem + 'iyorum'
    else:
        if (last_letter == last_vowel):
            small_stem = stem[:-1]
        else:
            small_stem = stem

        return small_stem + dict[person][last_vowel]


persons = ['1sg']
#, '2sg', '3sg', '1pl', '2pl', '3pl']

words = {"havlamak": {'1sg': "havlıyorum"},
         "bulmak":  {'1sg': "buluyorum"},
         "aramak": {'1sg': "arıyorum"}}

for person in persons:

    for word, expected in words.items():
        # conjugate the word
        conjugated = conjugate(word, person)

        # compare the result with the expected
        expected_person = expected[person]

        if (conjugated != expected_person):
            print(f'Error for {word}. Expected: {expected_person}, '
                  f'but got {conjugated}')
        else:
            print(f'Conjugation for {word} is correct: {conjugated}')