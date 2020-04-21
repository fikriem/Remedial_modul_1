# Soal 1
# Buatlah suatu fungsi yang mengembalikan panjang terpendek dari suatu string
# kata yang terpisahkan oleh spasi (20 Point)
# Note: Kembalikan panjang dari kata yang terpendek, bukan katanya yang dikembalikan

def find_short(text):
    split = text.split()
    jumlah_kata = []
    for item in split:
        jumlah_kata.append(len(item))
    jumlah_kata.sort()
    print(jumlah_kata[0])

find_short("Many people get up early in the morning ")
print('\n')
find_short("Every office would getting newest monitor ")
print('\n')
find_short("Create new file after this morning")

# Soal 2
# Buatlah suatu fungsi yang menerima parameter angka positif, dan mengembalikan
# total berapa kali harus dikalikan digit dari angka tersebut hingga mencapai 1 digit
# (20 Point).


def persistence(n):
    if n>0:
        total = n
        step = 0
        while (total >= 10):
            state = total
            sisa = str(state)
            pembagian = 1
            for item in range (len(sisa)):
                pembagian *= int(sisa[item])
            step += 1
            total = pembagian
        return print(step)
    else:
        print("angka harus positif")

persistence(39)
print('\n')
persistence(999)
print('\n')
persistence(4)

# soal 3
# Buatlah suatu fungsi yang menerima dimensi dari Rows x Columns, sebagai
# parameter untuk membuat tabel multipikasi dengan ukuran sesuai dari dimensi yang
# diberikan dimana setiap value di tabel row berikutnya adalah hasil perkalian value
# # di row pertama dengan row keberapa value tersebut berada (30 point)

def multiplication_table(row, col):
    for i in range(1, row+1):
        list_baru = []
        list_baru.append(i)
        for j in range (1, col):
            list_baru.append(i*(j+1))
        print(*list_baru)

multiplication_table(3,3)
print('\n')
multiplication_table(5,3)
print('\n')
multiplication_table(3,5)

# soal 4
# Buatlah suatu fungsi yang menerima string, dimana setiap huruf di string tersebut
# digantikan dengan posisinya di urutan alphabet. Bila ada string lain selain huruf
# alphabet, jangan dihiraukan (30 point). 

def alphabet_position(string):
    group = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
    'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
    temp = []
    kalimat = list(string.lower())
    for item in kalimat:
        if item in group.keys():
            temp.append(group[item])
        else:
            pass
    return print(*temp)

alphabet_position("The sunset sets at twelve o' clock.")
print('\n')
alphabet_position("it’s never too late to try")
print('\n')
alphabet_position("Have you done your homework?")
