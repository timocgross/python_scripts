# 'ç ğ ı ş' belki gerekileceğin harflerdir.

print('Insert the verb you want to conjugate.')
word = input()
new_word = word[:-3]
final_word = new_word[:-1]

# Present conjugation
print('Which person (f.e. 1. Sg.)?')
user_person = input()

if 'a' or 'ı' in final_word[-3:-1]:
    if user_person == '1. Sg.':
        present_i_pers_sg = final_word + 'ıyorum'
        print(present_i_pers_sg)
    elif user_person == '2. Sg.':
        present_ii_pers_sg = final_word + 'ıyorsun'
        print(present_ii_pers_sg)
    elif user_person == '3. Sg.':
        present_iii_pers_sg = final_word + 'ıyor'
        print(present_iii_pers_sg)
    elif user_person == '1. Pl.':
        present_i_pers_pl = final_word + 'ıyoruz'
        print(present_i_pers_pl)
    elif user_person == '2. Pl.':
        present_ii_pers_pl = final_word + 'ıyorsunuz'
        print(present_ii_pers_pl)
    elif user_person == '3. Pl.':
        present_iii_pers_pl = final_word + 'ıyorlar'
        print(present_iii_pers_pl)
    else:
        exit()
elif 'e' or 'i' in final_word[-3:-1]:
    if user_person == '1. Sg.':
        present_i_pers_sg = final_word + 'iyorum'
        print(present_i_pers_sg)
    elif user_person == '2. Sg.':
        present_ii_pers_sg = final_word + 'iyorsun'
        print(present_ii_pers_sg)
    elif user_person == '3. Sg.':
        present_iii_pers_sg = final_word + 'iyor'
        print(present_iii_pers_sg)
    elif user_person == '1. Pl.':
        present_i_pers_pl = final_word + 'iyoruz'
        print(present_i_pers_pl)
    elif user_person == '2. Pl.':
        present_ii_pers_pl = final_word + 'iyorsunuz'
        print(present_ii_pers_pl)
    elif user_person == '3. Pl.':
        present_iii_pers_pl = final_word + 'iyorlar'
        print(present_iii_pers_pl)
    else:
        exit()
elif 'o' or 'u' in final_word[-3:-1]:
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
elif 'ö' or 'ü' in new_word[-3:-1]:
    if user_person == '1. Sg.':
        present_i_pers_sg = new_word + 'üyorum'
        print(present_i_pers_sg)
    elif user_person == '2. Sg.':
        present_ii_pers_sg = new_word + 'üyorsun'
        print(present_ii_pers_sg)
    elif user_person == '3. Sg.':
        present_iii_pers_sg = new_word + 'üyor'
        print(present_iii_pers_sg)
    elif user_person == '1. Pl.':
        present_i_pers_pl = new_word + 'üyoruz'
        print(present_i_pers_pl)
    elif user_person == '2. Pl.':
        present_ii_pers_pl = new_word + 'üyorsunuz'
        print(present_ii_pers_pl)
    elif user_person == '3. Pl.':
        present_iii_pers_pl = new_word + 'üyorlar'
        print(present_iii_pers_pl)
    else:
        exit()
