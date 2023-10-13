operacion =input('¿que tipo de operacion desea realizar?')
n1 = int(input('ingrese el primer numero'))
n2 = int(input('ingrese el segundo numero'))
def operaciones(n1,n2,operacion):

   

     if operacion == '-':
        return  n1 - n2
        

     elif operacion == '*':
        return n1 * n2 
        

     if operacion == '/':
        return n1 / n2    
         

     elif operacion == '+':
        return n1 + n2 
       
     elif operacion== 'p':
        return n1 ** n2

   #al usar esta operacion mencione dos veces el numero que le quiere halla la raiz
     elif  operacion == '**':
         return n1 ** 0.5
     
        
   
resultado = operaciones(n1,n2,operacion)
def display_result():
    print('el resultado es:', resultado)
display_result()

texto = input('quieres seguir haciendo operaciones?').lower()
while texto == 'si':
    operacion =input('¿que tipo de operacion desea realizar?')
    n1 = int(input('ingrese el primer numero'))
    n2 = int(input('ingrese el segundo numero'))
    operaciones(n1,n2,operacion)
    display_result()
    texto = input('quieres seguir haciendo operaciones?')
