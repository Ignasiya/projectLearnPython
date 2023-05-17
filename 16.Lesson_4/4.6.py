# num = [1, 3, 6, 8, 11]
# data = open('file.txt', 'a')
# data.writelines(num)
# data.close()

with open('file.txt', 'w') as txt_file:
    txt_file.write('line 1\n')
    txt_file.write('line 2\n')

path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()