import numbers
def llave(p1,p2):
  #dos numeros primos
  p1=p1
  p2=p2
  
  #multiplicar
  n=p1*p2

  #obtener mcd
  minc=mcd(p1-1,p2-1)
  #obtener el coprimo de minc. segundo valor el min. se obtiene el cercano
  cop(minc,1)
  print(1%780)
  print(413*17)


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

def cop(num,ini):
  i=ini
  while (True):
    check=num/i
    if(int(check)!=check):
      break
    i+=1
  return check

llave(61,53)
