class BinaryUtils:
    @staticmethod
    def binaryArrayToDecimal(binaryArray):
        return sum([el * 2 ** index for index, el in enumerate(binaryArray[::-1])])

class BinaryNumber:
    def __init__(self, decimalNumber):
        self._number = []
        numberRemainder = decimalNumber
        while numberRemainder > 0:
            self._number.insert(0, numberRemainder % 2)
            numberRemainder = numberRemainder // 2

    def binary(self):
        return self._number.copy()

    def decimal(self):
        return BinaryUtils.binaryArrayToDecimal(self.binary())

class RijndaelFieldElement:
    _definingPolynomialBinary = BinaryNumber(282)

    def __init__(self, binaryNumber):
        self.binaryRepresentation = binaryNumber

    def multiply(self, multiplier):
        return RijndaelFieldElement(BinaryNumber(
            (self.binaryRepresentation.decimal() * multiplier.binaryRepresentation.decimal()) % self._definingPolynomialBinary.decimal()
        ))

    def stringRepr(self):
        return ' + '.join(
            [f'x^{7 - obj["index"]}' for obj in
                [{'index': index, 'include': binaryDigit == 1} for index, binaryDigit
                    in enumerate(self.binaryRepresentation.binary())
                ]
                if obj['include']
            ]
        )