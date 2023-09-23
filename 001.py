print ('Ey, du da! Wie heißt du?')
MyName = input()
print ('Oke, und wie alt bist du?')
MyAge = input()
print ('Hum, lass mich raten, du bist ' + str (2023 - int(MyAge)) + ' geboren?')
if input() == 'Ja' or 'ja':
   print ('Hehe')
else:
   print ('Wie kannst du das denn nicht wissen?')