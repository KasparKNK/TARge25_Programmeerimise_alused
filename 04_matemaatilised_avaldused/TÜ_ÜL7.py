"""
Koosta programm, mis küsib kasutajalt arvu N ja väljastab O-tähtedest koosneva ruudu suuruses NxN.
Seejärel muutke programmi nii, et ruudu diagonaalidel olevad märgid oleksid X-d.
"""

def draw_square(size: int, symbol: int):
    for row in range(size):
        for col in range(size):
            if row == col or row + col == size - 1:
                print(f"{alt}",end=" ")
            else:
                print(f"{symbol}",end=" ")
        print()

if __name__ == '__main__':
    size = int(input("Kui suur ruutu soovid? "))
    draw_square(size, "o", "x")
    draw_square(size * 2, "I", "-")