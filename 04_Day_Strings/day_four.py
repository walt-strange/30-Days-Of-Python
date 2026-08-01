string = 'Thirty' + ' ' + 'Days' + ' ' + 'of' + ' ' + 'Python'
print(string)
second_string = 'Coding' + ' ' + 'for' + ' ' + 'all'
print(second_string)

company = 'Coding For All'
print(company)

print(len(company))
print(company.upper())
print(company.lower())
print(company.title())
print(company.swapcase())
print(company.capitalize())
print(company.replace('Coding', 'Fun'))

second_company = 'Python for Everyone'
print(second_company.replace('Everyone', 'all'))

print(company.split(' '))

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

print(company[0]) 

print(company[-1])

print(company[0] + company[7] + company[11])
print(second_company[0] + second_company[7].upper() + second_company[11])

print(company.index('C'))
print(company.index('F'))
print(company.rindex('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'

print(sentence.find('because'))
print(sentence[0:sentence.find('because')] + sentence[sentence.rfind('because'):(len(sentence))])

print(company.startswith('Coding'))
print(company.endswith('coding'))

company = '   Coding For All      '
print(company.strip(' '))

libraries =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(libraries))

print('I am enjoying this challenge.\nI just wonder what is next.')

print('Name\t Age\tCountry\tCity')
print('Asabeneh 250\tFinland\tHelsinki')

radius = int(input('Input radius: '))
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))

a = 8
b = 6

print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')