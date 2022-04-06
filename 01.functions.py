#Ejemplo de una funcion sin valor de retorno
def volume(radius):
    v = 4/3 * 3,14 * radius ** 3
    print(v)


enigma = volume(7)
print(enigma)


#Ejemplo de una funcion con valor de retorno
def area(radius):
    a = 3,14 * radius ** 2
    return a


resultado = area(7)
area(7) #Este computo se perdio para siempre ya que no se asigno a ninguna variable
print(resultado)

#Podemos tener mas de un retorno por función
def isAdult(age):
    if age < 18:
        return False
    if age >= 18:
        return True

hasBeer = isAdult(18)
print(hasBeer)
