import numbers,random,math

#https://en.wikipedia.org/wiki/RSA_(cryptosystem)
def llave(p1,p2):
  n=p1*p2

  minc=mcd(p1-1,p2-1)

  publica=cop(minc,1)
  privada=modmulinv(17,780)

  return publica,privada,n

#Rivest R., Shamir A., Adleman L (1978). A Method for Obtaining Digital Signatures and Public-key Cryptosystems.
#Communications of the ACM. 21(2). 120-126
def llave2(p1,p2):
  n=p1*p2
  i=max(p1,p2) + random.randint(0,n)
  n2=(p1-1)*(p2-1)
  while (True):
    if(math.gcd(i,n2)==1):
      break
    i+=1
  public=i
  private=modmulinv(i,n2)
  return public,private,n

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


while True:
  #publica,privada,mod=llave(61,53)
  print("primos 47 y 59 para prueba rapida")
  p1=int(input("Ingrese un numero primo "))
  p2=int(input("Ingrese un segundo numero primo "))
  publica,privada,mod=llave2(p1,p2)
  print("")
  print("llave publica=",publica)
  print("llave privada=",privada)
  print("mod=",mod)
  txt=int(input("ingrese numero a encriptar "))
  msj=encriptar(txt,privada,mod)
  print("numero encriptado=",msj)
  print("numero desencriptado=",descrifrar(msj,publica,mod))
  input("ingrese un valor alfanumerico para continuar")
  break
