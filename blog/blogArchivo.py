import os

import csv

##########################
# CLASES


class Nota:
    def __init__(self, nota):

        self.nota = nota


class Bloc:
    def __init__(self):
        self.bloc = []  # publico

    # METODOS

    def nueva(self, nota):
        entrada = Nota(nota)
        self.bloc.append(entrada)
        self._guardar()

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

    def _guardar(self):
        with open('blog.txt', 'w') as f:
            writer = csv.writer(f)
            # Nombre que le damos a las columnas
            # writer.writerow('nota')

            # # escribir contacto por filas
            for contact in self.blog:
                writer.writerow(contact.nota)


def run():
    os.system('clear')
    bloc_de_Julia = Bloc()


    # with open('file.txt', 'r') as f:
#     for linea in f:
#         print(linea)

    with open('blog.txt', 'r') as f:
        for linea in f:
            print(linea)

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
                    nota = input('Introduce tu nota ')
                    bloc_de_Julia.nueva(nota)
                    

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
                            id_nota = int(
                                input('Introduce el identificador de la nota a borrar '))
                            bloc_de_Julia.borrar(id_nota)

                            # Vuelvo a mostrar las notas si es que hay alguna
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
