list = ['blue', 'green', 'red', 'purple', 'pink', 'orange', 'grey']
limit = input('Enter a number: ')
string = ''
count = 0
if limit == '':
    for i in list:
        string = string + '\n' + i
        count = count + 1
    print('The count is: ', count, 'and the string is: ', string)
else:
    limit = int(limit)
    for i in list[:limit]:
        string = string + '\n' + i
        count = count + 1
    print('The count is: ', count, 'and the string is: ', string)