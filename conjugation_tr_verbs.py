# 'ç ğ ı ş' belki gerekileceğin harflerdir.

print('Insert the verb you want to conjugate.')
# word = input()
word = "bulmak"
stem = word[:-3]
final_word = stem[:-1]

# Present conjugation
print('Which person (f.e. 1. Sg.)?')
# user_person = input()
user_person = "1. Sg."

if 'a' in stem or 'ı' in stem:
    if user_person == '1. Sg.':
        present_i_pers_sg = stem + 'ıyorum'
        print(present_i_pers_sg)
    elif user_person == '2. Sg.':
        present_ii_pers_sg = stem + 'ıyorsun'
        print(present_ii_pers_sg)
    elif user_person == '3. Sg.':
        present_iii_pers_sg = stem + 'ıyor'
        print(present_iii_pers_sg)
    elif user_person == '1. Pl.':
        present_i_pers_pl = stem + 'ıyoruz'
        print(present_i_pers_pl)
    elif user_person == '2. Pl.':
        present_ii_pers_pl = stem + 'ıyorsunuz'
        print(present_ii_pers_pl)
    elif user_person == '3. Pl.':
        present_iii_pers_pl = stem + 'ıyorlar'
        print(present_iii_pers_pl)
    else:
        exit()
elif 'e' in stem or 'i' in stem:
    if user_person == '1. Sg.':
        present_i_pers_sg = stem + 'iyorum'
        print(present_i_pers_sg)
    elif user_person == '2. Sg.':
        present_ii_pers_sg = stem + 'iyorsun'
        print(present_ii_pers_sg)
    elif user_person == '3. Sg.':
        present_iii_pers_sg = stem + 'iyor'
        print(present_iii_pers_sg)
    elif user_person == '1. Pl.':
        present_i_pers_pl = stem + 'iyoruz'
        print(present_i_pers_pl)
    elif user_person == '2. Pl.':
        present_ii_pers_pl = stem + 'iyorsunuz'
        print(present_ii_pers_pl)
    elif user_person == '3. Pl.':
        present_iii_pers_pl = stem + 'iyorlar'
        print(present_iii_pers_pl)
    else:
        exit()
elif 'o' in stem or 'u' in stem:
    if user_person == '1. Sg.':
        present_i_pers_sg = final_word + 'uyorum'
        print(present_i_pers_sg)
    elif user_person == '2. Sg.':
        present_ii_pers_sg = final_word + 'uyorsun'
        print(present_ii_pers_sg)
    elif user_person == '3. Sg.':
        present_iii_pers_sg = final_word + 'uyor'
        print(present_iii_pers_sg)
    elif user_person == '1. Pl.':
        present_i_pers_pl = final_word + 'uyoruz'
        print(present_i_pers_pl)
    elif user_person == '2. Pl.':
        present_ii_pers_pl = final_word + 'uyorsunuz'
        print(present_ii_pers_pl)
    elif user_person == '3. Pl.':
        present_iii_pers_pl = final_word + 'uyorlar'
        print(present_iii_pers_pl)
    else:
        exit()
elif 'ö'in stem[-3:-1] or 'ü' in stem[-3:-1]:
    if user_person == '1. Sg.':
        present_i_pers_sg = stem + 'üyorum'
        print(present_i_pers_sg)
    elif user_person == '2. Sg.':
        present_ii_pers_sg = stem + 'üyorsun'
        print(present_ii_pers_sg)
    elif user_person == '3. Sg.':
        present_iii_pers_sg = stem + 'üyor'
        print(present_iii_pers_sg)
    elif user_person == '1. Pl.':
        present_i_pers_pl = stem + 'üyoruz'
        print(present_i_pers_pl)
    elif user_person == '2. Pl.':
        present_ii_pers_pl = stem + 'üyorsunuz'
        print(present_ii_pers_pl)
    elif user_person == '3. Pl.':
        present_iii_pers_pl = stem + 'üyorlar'
        print(present_iii_pers_pl)
    else:
        exit()
