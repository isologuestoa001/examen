encriptado = input() 
while(1):
  freq = {}
 
  for i in encriptado:
   if i.isalpha():
     if i in freq:
         freq[i] += 1
     else:
         freq[i] = 1
  a= dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
 
  print(str(a))
  letra_original = input("Introduce la letra que deseas reemplazar: ")
  nueva_letra = input("Introduce la letra con la que deseas reemplazarla: ")
  encriptado = encriptado.replace(letra_original, nueva_letra)
  print(encriptado)
