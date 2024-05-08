import os
import time

limpieza_pantalla = "cls"
mientras1 = 1
seleccion = 0
prod1 = 0
prod2 = 0
prod3 = 0
prod4 = 0
totalprod1 = 0
totalprod2 = 0
totalprod3 = 0
totalprod4 = 0

while mientras1 == 1
os.system("cls")
time.sleep(1)

while mientras1 != 5:
    print("Bienvenido a Delivery Sushi")
    print("Seleccione entre las siguientes opciones los rolls que desea agregar")
    print("1. Pikachu Roll - $4.500 c/u")
    print("2. Otaku Roll - $5.000 c/u")
    print("3. Pulpo Venenoso Roll $5.200 c/u")
    print("4. Anguila Electrica Roll - $4.800 c/u")
    print("5. Terminar compra")
    print("6. Salir")

    try:
        seleccion = int(input("Seleciona una opcion entre 1-5: "))
    except ValueError:
        print("Selecciona una opcion entre 1-5, ya que la elegida es incorrecta")
        continue

    if seleccion == 1:
        try:
            prod1 = int(input("Has seleccionado Pikachu Roll, por favor indique cuantos desea"))
        except ValueError:
            print("La seleccion debe ser entre 1-4: ")
            continue
        totalprod1 = prod1*4500
        continue
       


