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
  publica=cop(minc,1)
  privada=modmulinv(17,780)

  return publica,privada,minc

def modmulinv(num,modulus):
  i=1
  while (True):
    if((num*i)%modulus==1):
      return i
    i+=1

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

def procesar(num,llave,mod):
  return (((num)**llave)%mod)

def encriptar(num,llavePrivada,mod):
  return (((num)**llavePrivada)%mod)

def descrifrar(num,llavePublica,mod):
  return(((num)**llavePublica)%mod)

publica,privada,mod=llave(61,53)

