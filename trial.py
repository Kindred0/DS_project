f = open('196146.png', 'rb')

i = 1
for lines in f :
    print('line', i)
    i = i + 1
    print(lines)

file = open('file.png', 'wb' )

for lines in f :
    file.write(lines)

f.close()
file.close()