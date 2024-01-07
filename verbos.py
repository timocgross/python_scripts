from verbos_irregulares import irregulares
from verbos_classes import classes

verb = input('Coloque um verbo: ')

if verb in irregulares:
    tempo = input('Tempo: ')
    if tempo == 'Particípio':
        gênero = input('Gênero: ')
        número = input('Número: ')
        print(irregulares[verb][tempo][gênero][número])
    elif tempo == 'Gerúndio':
        print(irregulares[verb]['Gerúndio'])
    else:
        pessoa = input('Pessoa: ')
        print(irregulares[verb][tempo][pessoa])

elif verb[-2:] == 'ar':
    verb_class = 'ar'
    print(f'O verbo "{verb}" pertence à classe "-{verb_class}".')
    tempo = input('Tempo: ')
    if tempo == 'Particípio':
        gênero = input('Gênero: ')
        número = input('Número: ')
        print(verb[:-2] + classes['primeira_ar']['Particípio'][gênero][número])
    elif tempo == 'Gerúndio':
        print(verb[:-2] + classes['primeria_ar']['Gerúndio'])
    elif tempo == 'Presente':
        pessoa = input('Pessoa: ')
        if verb[-3] == 'e':
            if pessoa == '1sg':
                print(verb[:-2] + 'io')
            elif pessoa == '2sg' or '3sg':
                print(verb[:-2] + 'ia')
            elif pessoa == '2pl' or '3sg':
                print(verb[:-2] + 'iam')
            else:
                print(verb[:-2] + classes['primeira_ar']['Presente'][pessoa])
    elif tempo == 'Pretérito':
        pessoa = input('Pessoa: ')
        if verb[-3] == 'g':
            if pessoa == '1sg':
                print(verb[:-2] + 'uei')
        elif verb[-3] == 'c':
            if pessoa == '1sg':
                print(verb[:-3] + 'quei')
        elif verb[-3] == 'ç':
            if pessoa == '1sg':
                print(verb[:-3] + 'cei')
        else:
            print(verb[:-2] + classes['primeira_ar']['Pretérito'][pessoa])
    elif tempo == 'Subjuntivo presente':
        pessoa = input('Pessoa: ')
        if verb[-3] == 'c':
            print(verb[:-3] + 'qu' + classes['primeira_ar']['Subjuntivo presente'][pessoa])
        elif verb[-3] == 'ç':
            print(verb[:-3] + 'c' + classes['primeira_ar']['Subjuntivo presente'][pessoa])
        elif verb[-3] == 'e':
            print(verb[:-2] + 'i' + classes['primeira_ar']['Subjuntivo presente'][pessoa])
        else:
            print(verb[:-2] + classes['primeira_ar']['Subjuntivo presente'][pessoa])
    else:
        pessoa = input('Pessoa: ')
        print(verb[:-2] + classes['primeira_ar'][tempo][pessoa])

elif verb[-2:] == 'er':
    verb_class = 'er'
    print(f'O verbo "{verb}" pertence à classe "-{verb_class}".')
    tempo = input('Tempo: ')
    if tempo == 'Particípio':
        gênero = input('Gênero: ')
        número = input('Número: ')
        print(verb[:-2] + classes['segunda_er']['Particípio'][gênero][número])
    elif tempo == 'Gerúndio':
        print(verb[:-2] + classes['segunda_er']['Gerúndio'])
    elif tempo == 'Presente':
        pessoa = input('Pessoa: ')
        if verb[-3] == 'c':
            if pessoa == '1sg':
                print(verb[:-3] + 'ço')
        else:
            print(verb[:-2] + classes['segunda_er']['Presente'][pessoa])
    elif tempo == 'Subjuntivo presente':
        pessoa = input('Pessoa: ')
        if verb[-3] == 'c':
            print(verb[:-3] + 'ç' + classes['segunda_er']['Subjuntivo presente'][pessoa])
        else:
            print(verb[:-2] + classes['segunda_er']['Subjuntivo presente'][pessoa])
    else:
        pessoa = input('Pessoa: ')
        print(verb[:-2] + classes['segunda_er'][tempo][pessoa])

elif verb[-2:] == 'ir':
    verb_class = 'ir'
    print(f'O verbo "{verb}" pertence à classe "-{verb_class}".')
    tempo = input('Tempo: ')
    if tempo == 'Particípio':
        gênero = input('Gênero: ')
        número = input('Número: ')
        print(verb[:-2] + classes['terceira_ir']['Particípio'][gênero][número])
    elif tempo == 'Gerúndio':
        print(verb[:-2] + classes['terceira_ir']['Gerúndio'])
    else:
        pessoa = input('Pessoa: ')
        print(verb[:-2] + classes['terceira_ir'][tempo][pessoa])
