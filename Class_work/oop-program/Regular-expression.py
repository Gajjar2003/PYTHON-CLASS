import re

# match expression 

m = re.match('n.l',"nil hello")  # match use to be beginning string allowed
print(m)

print("****************************************")


# search expression

k = re.search('n.l',"anil pytholn") # sreach use to be all string search 
print(k)


print("****************************************")

# findall expression

f = re.findall('j.n',"jenil hello") # findall use to be find a string and output 
print(f)


print("****************************************")

k = re.match('^hello',"hello python")
print(k)

k = re.search('jenil$',"hello jenil")
print(k)

k = re.findall('[0-9]',"hello 1 to 9 python")
print(k)

k = re.findall('\W',"Hello pyt @ 1 Ho 3ln abc")
print(k)

k = re.findall('la{2}l',"Helaaalo pyt @ 1 Ho 3ln abc")
print(k)