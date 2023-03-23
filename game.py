from random import choise, randrange
from datetime import datetime
#Operadores posibles
operators=["+","-","*","*"]
#cantidad de cuentas a resolver
times = 5
#contador inicial de tiempo
#esto toma la fecha y hora actual
init_time= datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
correctas =0
for i in range(0, times):
    #se eligen numeros y operador al azar
    number_1=randrange(10)
    number_2=randrange(10)
    operator=choise(operators)
    #se imprime la cuenta
    print(f"{i+1}-¿Cuanto es {number_1} {operator} {number_2} ?")
    #le pedimos al usuario el resultado
    result=input("resultado: ")

    if(operator=='+'):
        res=number_1 + number_2
    elif(operator=='-'):
        res=number_1 - number_2
    elif(operator=='*'):
        res=number_1 * number_2
    elif(operator=='/'):
        if(number_2==0):
            print('No se puede dividir por cero')
        else:
           res=number_1 / number_2
    if(result==res):
        print('Respuesta correcta')
        #contador de respuestas correctas
        correctas+=1
    else:
        print('resouesta incorrecta')
print(f"Hubo {correctas} respuestas correctas")
incorrectas=times-correctas
print(f"Hubo {incorrectas} respuestas incorrectas")
#Al terminar toda la cantidad de cuentas por resolver.
#Se vuelve a tomar la fecha y la hora.
end_time=datetime.now()
#Restando las fechas obtenemos el tiempo transcurrido.
total_time=end_time-init_time
#Mostarmos ese tiempo en segundos.
print(f"Tardaste {total_time.seconds} segundos.")

