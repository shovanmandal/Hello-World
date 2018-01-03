import math

n= input('give input:')
x = math.floor(math.sqrt(int(n)))
lesser_sqr = x * x
print(lesser_sqr)
if lesser_sqr != n:
    print('input is not a square')
greater_sqr = (x+2)*(x+2)
print(greater_sqr)




A = [['','','',''],
     [5,4,3,''],
     [6,1,2,''],
     [7,8,'','']]
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in A]))
