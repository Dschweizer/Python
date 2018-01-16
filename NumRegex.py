import re
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4253.')
print(mo.group(1)) #print first part of number

print(mo.group(2)) #print second part

print(mo.group(0)) #print all of the number

print(mo.group())  #again prints all of the number

mo.groups()
areaCode, mainNumber = mo.groups() #Assign area code
print('This is the area code for this number: ' + areaCode)

print('This is the main number: ' + mainNumber)
