line = input('Enter a poem line: ')
print('Length of the line is {0}'.format(len(line)))
l, r = [int(num) for num in input('Enter left and right ends of a segment: ').split()]
print(line[l-1:r])
