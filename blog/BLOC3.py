import csv


class Nota:

    def __init__(self, name):
        self.name = name


class Blog:

    def __init__(self):
        self._blog = []

    def add(self, name):
        nota = Nota(name)
        self._blog.append(nota)
        self._save()

    def _save(self):
        with open('blog.csv', 'a') as f:
            writer = csv.writer(f)
            # # escribir contacto por filas
            for entrada in self._blog:
                # print(nota.name)
                f.write(entrada.name)
                # writer.writerow(entrada.name)
                # f.writer(f'{nota.name}\n')

                # writer.writerow(nota.name)
        #     # Nombre que le damos a las columnas
        #     # writer.writerow( 'Nombre' )
    # def show_all(self):
    #     for contact in self._contacts:
    #         self._print_contact(contact)

    def show_all(self):
        for nota in self._blog:
            self._print_nota(nota)

    def _print_nota(self, nota):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nota: {}'.format(nota.name))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

        # print(self._blog)


def run():

    contact_book = Blog()

    with open('blog.csv', 'r') as f:
        reader = csv.reader(f)

    #     for idx, line in enumerate(reader):

    #         if idx == 0:
    #             continue

    #         contact_book.add(line[0])

    while True:

        command = str(input('''
            ¿Qué deseas hacer?
            [a]ñadir nota

            [l]istar notas
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe tu nota: '))

            contact_book.add(name)

        elif command == 'l':

            contact_book.show_all()

        elif command == 's':
            f.close()
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('BLOC DE NOTAS')
    run()
