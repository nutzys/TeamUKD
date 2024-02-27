x = int(input('Input Hours: '))

y = float(input('Input Rate: '))
if x<=40:
    pay=(x*y)
else: 
    pay =(40*y+(x-40)*y*1.25)

print('Pay: ', pay)


