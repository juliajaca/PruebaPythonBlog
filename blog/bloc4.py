import csv


class Entrada:
    def __init__(self, nota):
        self.nota = nota


class EntradaBook:

    def __init__(self):
        self._contacts = []

    def add(self, nota):
        contact = Entrada(nota)
        print(contact.nota)
        self._contacts.append(contact)
        print(self.contacts)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def _save(self):
        with open('blog.csv', 'w') as f:
            writer = csv.writer(f)

            # escribir por filas
            for contact in self._contacts:
                writer.writerow((contact.nota))

    def _print_contact(self, contact):

        print('NOTA: {}'.format(contact.nota))



def run():

    contact_book = EntradaBook()

    with open('blog.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            contact_book.add(row[0])

    while True:

        command = str(input('''
            ¿Qué deseas hacer?
            [a]ñadir contacto
            [l]istar contact
            [s]alir
        '''))

        if command == 'a':
            nota = str(input('Escribe el nombre del contacto: '))

            contact_book.add(nota)

        elif command == 'l':

            contact_book.show_all()

        elif command == 's':
            f.close()
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O  AL BLOC')
    run()
