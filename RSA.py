def llave(p1,p2):
  #dos numeros primos
  p1=p1
  p2=p2
  
  #multiplicar
  n=p1*p2
  print(mcd(p1-1,p2-1))


def mcd(num1,num2):

  if(num1>num2):
    alto=num1
  else:
    alto=num2
  
  while(True):
    if((alto%num1==0) and (alto%num2==0)):
      break
    else:
      alto+=1
  return alto

llave(61,53)
