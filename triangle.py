import math  

def main():
    A = int(input("What is the length of side A"))
    B = int(input("What is the length of side B"))
    pythag(A,B)
   


def pythag(A,B):
    Asqaured = A * A
    Bsqaured = B * B
    C = Asqaured + Bsqaured
    result = math.sqrt(C)
    print(result)

main()