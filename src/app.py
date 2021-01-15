import json
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
cola = queue.get_queue()

def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())

def add():
    cola = queue.get_queue()
    name = input("introducir nombre del usuario: \n")
    number = input("introducir numero de teléfono: \n")

    client= {
        "name" : name,
        "number" : number,
        "position": len(cola)+1
    }
    cola.append(client)
    return cola

def dequeue():
    cola = queue.get_queue()
    #una manera de recorrer el objeto
    for diccionario in cola:
        nombre=diccionario["name"]
        posicion=diccionario["position"]
        telefono=diccionario["number"]
        print(f"({posicion}) nombre: {nombre} y tlf: {telefono}")

    opcion = 1  #int(input("cual borrar? \n")) #al borrar al primero automáticamente se comporta como FIFO
                #si se descomenta, se le estaría dando la opción al usuario de borrar
                #según la "position", pero podría ser "name" o "number"
    colaFiltrada = [index for index in cola if index["position"] != opcion]
    cola.clear()
    for index in colaFiltrada:
        cola.append({"name":index["name"],"number":index["number"],"position":len(cola)+1})
    print(cola)
    return cola

    

def save():
    pass

def load():
    pass 
        
    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 3:
        print_queue()
    elif option == 1:
        add()
        print_queue()
    elif option ==2:
        dequeue()
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
