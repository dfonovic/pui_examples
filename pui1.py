a = eval(input('unesi broj a:'))
if a < 0:
	print("Broj je negativan")
	print("Apsolutna vrijednost: ", -a)
else:
	print("Broj je pozitivan")
	print("Apsolutna vrijednost je: ", a)
print("Kraj")
'''
#primjer zamjene dvije verijable
x = int(input('unesite prvi broj:'))
y = int(input('unesite drugi broj:'))
print('prije zamijene:', x,y)
temp = x #nova varijabla u koju ćemo privremeno smjestiti vrijednost x
x = y # x dobiva vrijednost od y
y = temp # y dobiva vrijednost od x
print('nakon zamjene:', x,y)
'''
'''
#isti primjer korištenjem funkcije
def zamijeni(x,y):
    return y,x
x = int(input('unesite prvi broj:'))
y = int(input('unesite drugi broj:'))
print('prije zamijene:', x,y)
x,y = zamijeni(x,y)
print('nakon zamjene:', x,y)
'''
'''
#primjer funkcije za kreiranje polja slučajnih cijeli brojeva u rasponu od 1 - 100
import random

def generiraj_listu(n):
    for i in range(n):
        x = random.randint(1,100)
        lista.append(x)

n = int(input('unesite velicinu polja:'))
lista = []
generiraj_listu(n)
print(lista)
'''
'''
#primjer .join() metode za rad sa stringovima
# sintaksa metode .join():   string.join(iterable)
lista = ['PROGRAMIRANJE','U','INZENJERSTVU']
separator = '-@-'
str = separator.join(lista)
print (str)
'''
'''
#program za generiranje passworda
import random
import string #primjer korištenja string modula možete pogledati na linku: https://pymotw.com/2/string/

slova = string.ascii_letters

brojevi = '0123456789'
#specijalni = '!$#?'  možemo dodati i ovo ako želimo imati i specijalne znakove

znakovi = slova + brojevi # + specijalni

duljina = int(input("unesite duzinu passworda:"))

password = ''.join(random.sample(znakovi, duljina))

print(password)
'''
'''
#program za pogađanje zamišljenog broja
import random

x = random.randrange(1, 20)

while True:
  guess = int(input("unesi broj: "))

  if guess == x:
    print ("pogodak!")
    break
  elif guess < x:
    print ("broj je veci")
  else:
    print ("broj je manji")
print('kraj')

'''
'''
#primjer pretraživanja polja
'''
'''
primjer korištenja modula time
štoperica
brojač
'''


