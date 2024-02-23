j = int(input('Enter a number: '))

class Conversions:
    def __init__(self, j):
        self.j = j

    def binary(self):
        bin_number = bin(self.j)
        print(f'The binary number is {bin_number}.')

    def octal(self):
        oct_number = oct(self.j)
        print(f'The octal number is {oct_number}.')

    def hexadecimal(self):
        hex_number = hex(self.j)
        print(f'The hexadecimal number is {hex_number}.')

c1 = Conversions(j)
c1.binary(); c1.octal(); c1.hexadecimal()
