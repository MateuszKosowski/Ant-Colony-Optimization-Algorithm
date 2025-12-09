class Place:

    def __init__(self, number, x, y):
        self.number = number
        self.position = (x, y)


class Places:

    def __init__(self, file_to_load):
        self.places_list = list()
        self.load_from_file(file_to_load)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split()
                        if len(parts) == 3:
                            number = int(parts[0])
                            x = int(parts[1])
                            y = int(parts[2])
                            place = Place(number, x, y)
                            self.places_list.append(place)
        except FileNotFoundError:
            print(f"Błąd: Nie znaleziono pliku {filename}")
        except Exception as e:
            print(f"Błąd podczas wczytywania pliku: {e}")


