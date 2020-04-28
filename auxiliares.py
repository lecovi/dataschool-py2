# Este módulo contiene diferentes funciones para importar y usar en módulos.ipynb

def imprimir_mensaje():
        """Esta función sólo imprime un mensaje en pantalla.
        """
        print("Hola! Simplemente vine a imprimir esto")
        print("Chau")

def saludo(nombre, apellido):
        """Recibe el nombre y apellido de una persona e imprime un saludo
        personalizado.
        """
        print(f"Bienvenido {nombre} {apellido}")

def saludo2(nombre, apellido, mensaje="Hola"):
        """Recibe el nombre y apellido de una persona e imprime un saludo 
        personalizado.
        Puede recibir un tercer argumento de texto que es lo que ante-
        cede al nombre y al apellido de la persona.
        """
        print(f"{mensaje} {nombre} {apellido}")

def saludo3(nombre, *args, **kwargs):
        """Imprime en pantalla el segundo argumento de texto recibido y
        el nombre a continuación.
        En la línea siguiente imprime el tercer argumento recibido.
        Y para terminar imprime el mensaje pasado como despedida.
        """
        print(f"{args[0]} {nombre}")
        print(args[1])
        print(kwargs['despedida'])

def incrementar(valor):
        """Incrementa el valor recibido y lo imprime en pantalla.
        Es importante destacar que no devuelve este valor.
        Modifica el argumento por valor.
        """
        valor = valor + 1
        print(valor)

def agregar(valor, lista):
        """Agrega el valor a la lista pasada.
        Es importante destacar que no devuelve ningún valor.
        Modifica el argumento por referencia.
        """
        lista.append(valor)
