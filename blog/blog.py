'''
Blog de notas de Julia
---------------------
v1.0
=======================
Ejercicio que puntúa hasta 3 puntos para el examen final del módulo
Sin internet
Sólo evernote
No hay slack
Para terminal
Pensar bien las  opciones que tendra el blog de notas
Diagramacion wwww.lucidchart.com (diagrama de flujo)
En el entorno virtual de 3.7.4
git local
al finalizar el ejercicio a las 16:15 enviar enlace por github
'''

import os

import csv

##########################
# CLASES


class Nota:
    def __init__(self, id_nota, nota):
        self.id_nota = id_nota
        self.nota = nota


class Bloc:
    def __init__(self):
        self.bloc = []  # publico

    # METODOS

    def nueva(self, id_nota, nota):
        entrada = Nota(id_nota, nota)
        self.bloc.append(entrada)

        print('''
            >>>
            \tNota añadida correctamente
            <<<
        ''')

    def mostrar_todo(self):
        if len(self.bloc) == 0:
            print('No hay notas ')
            return False
        else:
            for i in self.bloc:
                self._mostrar(i)  # privada
            return True


    def _mostrar(self, i):
        print('*************************')
        print('*************************')
        print('ID:{} '.format(i.id_nota))
        print('-------------------------')
        print('Nota:{} '.format(i.nota))

    def borrar(self, id_nota):
            for i in self.bloc:
                if id_nota == i.id_nota:
                    self.bloc.remove(i)
                    print('''
                >>>
                \tNota borrada correctamente
                <<<
                ''')



def run():
    os.system('clear')
    bloc_de_Julia = Bloc()

    while True:
        principal = input('''
        ¿Qué deseas hacer?
​
        [c] ontinuar
        [s] alir
    
        ''')

        if principal == 'c':
            while True:
                menu = input('''
                ¿Qué deseas hacer?
        ​
                [a] ñadir
                [v] er notas
                [s] alir
            
                ''')

                if menu == 'a':
                    id_nota = int(input('Introduce un número identificador único para la nota '))
                    nota = input('Introduce tu nota ')
                    bloc_de_Julia.nueva(id_nota, nota)

                elif menu == 'v':
                    notas = bloc_de_Julia.mostrar_todo()
                    # print(notas)
                    while notas:
                        submenu = input('''
                        ¿Qué deseas hacer?
                        [b] orrar nota
                        [s] alir
                        ''')

                        if submenu == "b":
                            id_nota = int(input('Introduce el identificador de la nota a borrar '))
                            bloc_de_Julia.borrar(id_nota)

                            #Vuelvo a mostrar las notas si es que hay alguna
                            notas = bloc_de_Julia.mostrar_todo()

                        elif submenu == "s":
                            break
                        else:
                            print('Error! Vuelve a probar')

                elif menu == 's':
                    break
                else:
                    print('Error! vuelve a probar')
                
        elif principal == 's':
            break 
        else:
            print('Error! Vuelve a probar')

if __name__ == "__main__":
    run()
