import random
import string

znakovi = string.ascii_letters + string.digits

unos = eval(input('unesite duljinu lozinke u rasponu od 4 do 10 znakova:'))

###
while unos < 4 and unos > 10:
    print ('neodgovarajuća duljina lozinke, pokusajte ponovo.')
    unos = eval(input('unesite duljinu lozinke u rasponu od 4 do 10 znakova:'))

pwd = ''

pwd = ''.join(random.sample(znakovi,unos))

print (pwd)
