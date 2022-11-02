#Thorian.Perk
#02.11.2022
#harjutus10


#kuva failist korralikud IPd
import re

fh = open('mida.txt')
for line in fh:
    if re.search('^[A-Z0-9]+[A-Z]{1}', line):
         print(line,end='')

print(" ")
print("----------------------------------")
print(" ")
#kuva korralikud
import re

fh = open('mida.txt')
for line in fh:
    if re.search('(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9])$', line):
         print(line,end='')
