from random import *
from tkinter import *
from datetime import *

#----------------------------------Variables necesarias a ser reemplazadas porarchivo DB

numerosusados = []
ahorro = {}
resultado = ''
#----------------------------------Funciones

def tirarmoneda(lista,diccionario):
    randomNumber = randrange(1, 366)
    iteracióndelista = randomNumber in lista
    if iteracióndelista == True:
        resultado['text'] = 'ERROR: Try again'
    elif iteracióndelista == False:
        lista.append(randomNumber)
        diccionario['{}'.format(date.today())] = randomNumber
        ahorrado = randomNumber
        print(lista, diccionario)
        resultado['text'] = 'Hoy debés ahorrar:\n ${}'.format(str(ahorrado))


#----------------------------------Ventana
ventana = Tk()
ventana.geometry('450x350')
ventana.title('Ahorra un monto minimo por día...')
ventana.config(bg='white smoke')
ventana.iconbitmap('C:\\Users\\Usuario\\Desktop\\Programacion\\python\\projects\\ahorrador\\icono.ico')
#----------------------------------Etiqueta de Bienvenida
welcome = Label(text= 'Bienvenida a programa de ahorro', fg='black', bg='white smoke', font = ('Lucida Sans', 15, 'bold'))
welcome.pack(padx = 10, pady = 10)
#----------------------------------Botón
boton = Button(ventana, bg='white', text= 'Tirar la moneda', font = ('Roboto', 15, 'normal'), command = lambda: tirarmoneda(numerosusados,ahorro))
boton.pack(padx = 10, pady = 10)
#----------------------------------ahorro
resultado = Label(fg='black', bg='white smoke', font = ('Lucida Sans', 30, 'bold'))
resultado.pack(padx = 10, pady = 10)


ventana.mainloop()


