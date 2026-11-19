
def icao(letter):
    alphabet = {
        "A": "Alfa", "B": "Bravo", "C": "Charlie",
        "D": "Delta", "E": "Echo", "F": "Foxtrot",
        "G": "Golf", "H": "Hotel", "I": "India",
        "J": "Juliett", "K": "Kilo", "L": "Lima",
        "M": "Mike", "N": "November", "O": "Oscar",
        "P": "Papa", "Q": "Quebec", "R": "Romeo",
        "S": "Sierra", "T": "Tango", "U": "Uniform",
        "V": "Victor", "W": "Whiskey", "X": "X-ray",
        "Y": "Yankee", "Z": "Zulu"
    }
    return alphabet.get(letter.upper(), "Unknown")

name = input("Enter name: ")

for letter in name:
    print(letter.upper(), "-", icao(letter))
