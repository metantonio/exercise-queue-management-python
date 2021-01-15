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
    #print(queue.get_queue())
    for diccionario in cola:
        nombre=diccionario["name"]
        posicion=diccionario["position"]
        telefono=diccionario["number"]
        print(f"({posicion}) nombre: {nombre} y tlf: {telefono}")

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
    def write_json(data, filename='queue.json'): 
        with open(filename,'w') as jsonFile: 
            json.dump(data, jsonFile, indent=4) 
      
      
    with open('queue.json') as json_file: 
        data = json.load(json_file) 
      
        #temp = data["client"] 
  
        # python object to be appended 
        #y = cola
          
        # appending data 
        #temp.append(y) 
      
    write_json(cola)  

def load():
    #import json #must be avalaible
    # Opening JSON file 
    f = open('queue.json',) 

    # returns JSON object as a dictionary 
    data = json.load(f)
    cola.clear()

    for index in data:
        cola.append({"name":index["name"],"number":index["number"],"position":index["position"]})
    print(cola)    
    # Closing file 
    f.close() 
    print(data)


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
    elif option ==5:
        load()
    elif option ==4:
        save()    
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
