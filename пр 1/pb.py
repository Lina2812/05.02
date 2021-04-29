n = int(input(''))
result = 0
while (n > 0):
        dig = n % 10
        result = result + dig
        n = n//10
 
print('', result)
