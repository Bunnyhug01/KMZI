from components.RijndaelFieldElement import BinaryNumber, RijndaelFieldElement


def menu():
    r1 = RijndaelFieldElement(BinaryNumber(0xE4))
    r2 = RijndaelFieldElement(BinaryNumber(0x11))
    
    print(r1.multiply(r2).stringRepr())
        
if __name__ == "__main__":
    menu()