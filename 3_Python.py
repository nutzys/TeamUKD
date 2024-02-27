x = (input('Input Hours: '))
try:
    z = int(x)
except:
    z = -1
    print("Error, please enter numeric input")

y = (input('Input Rate: '))
try:
    i = int(y)
except:
    i = -1
    print("Error, please enter numeric input")

if z<=40:
    pay=(z*i)
else: 
    pay =(40*i+(z-40)*i*1.25)

print('Pay: ', pay)
