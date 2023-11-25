class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        self._encode = dict()
        self._decode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            decode = self.alphabet[(i - key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
            self._decode[letter] = encoded
            self._decode[letter.upper()] = encoded.upper()

        self._decode = {}

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        return ''.join([self._encode.get(char, char) for char in line])


key = int(input('Введите ключ:'))
cipher = Caesar(key)
line = input()
while line != '.':
    print(cipher.decode(line))
    line = input()