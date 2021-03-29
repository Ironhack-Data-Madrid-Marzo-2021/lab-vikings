import claseswar
import random
import time
import os
import sys
from IPython.display import clear_output


exit = False
opcion_menu = 0
num_warriors = 3

while not exit:

    print ('''

▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-------------------⚔⚔⚔⚔⚔⚔------------------
---------------------------------------------

1.- Jugar la guerra!!

2.- Opciones (Seleccina tu Guerra)

4.- Salir del programa.

---------------------------------------------
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
''')

    # esta opción es para que en caso de que el usuario haya introducido un valor distinto a los del menú, llamarle la atención a ello
    #if opcion_menu != 0:
    #    print ('Tienes que introducir una opción válida') 
        
    opcion_menu = claseswar.introduce_numero()

    if opcion_menu == 1:
        pass
        
    elif opcion_menu == 2:
        num_warrios = claseswar.menu_opciones()

    elif opcion_menu == 4:
        exit = True

    else:
        clear_output()

print ('HASTA PRONTO!!!!')
time.sleep(2)
