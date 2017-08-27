input_string = input('input an array of strings: ')
input_array = input_string.split(',')


m= max(len(x) for x in input_array)+2

print(m*'*')
for i in range(len(input_array)):
    print ('*'+input_array[i]+(m-len(input_array[i])-2)*' '+'*')

print(m*'*')