# string Method In Practicals

s = "jenil"
print(s)
print(type(s))

s = "gajjar"
print(len(s))

s = "JENIL"
print(s.lower())

s = "jenil"
print(s.upper())

s = "jenil gajjar"
print(s.title())

s = "jenilgajjar"
print(s.capitalize())

s = "jenil  "
print(s.strip())

s = "jenil gajjar"
print(s.split())

s = "Gajjar"
j = s.replace("j","J")
print(j)

s = "jenil"
s1 = "gajjar"
s2 = s.join(s1)
print(s2)

s = "jenil"
print(s.isalpha())

s = "11"
print(s.isdigit())

s = "jenil123"
print(s.isalnum())

s = "jenil"
print(s.startswith("j"))

s = "jenil"
print(s.endswith("l"))

s = "jenil"
print(s.zfill(10))

s = "jenil"
print(s.center(12))

s = "jenil"
print(s.find("l"))