##### KALKULATOR SEDERHANA #####

## fungsi berbagai operasi ##
def add(x, y):          #tambah
    return x + y

def subtract(x, y):     #kurang
    return x - y

def multiply(x, y):     #kali
    return x * y

def divide(x, y):       #bagi
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"
## akhir dari berbagai fungsi operasi ##


## pilihan operasi untuk user ##
print("pilih operasi: ")
print("1. tambah")
print("2. kurang")
print("3. kali")
print("4. bagi")

choice = input("pilih operasi(1/2/3/4): ")
## akhir dari pilihan operasi ##


## fungsi untuk cek, yang dimasukkan harus berupa angka ##
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("data yang dimasukkan harus berupa angka :)")
## akhir dari fungsi untuk cek ##


## berbagai kondisi(kemungkinan) beserta hasil ##
if choice in ['1','2','3','4']:
    num1 = get_number("masukkan angka pertama: ")
    num2 = get_number("masukkan angka kedua: ")

    if choice == "1":
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")

    elif choice == "2":
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")

    elif choice == "3":
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")

    elif choice == "4":
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

else:
    print("Pilihan tidak valid. Silakan pilih antara 1, 2, 3, atau 4.")
## akhir berbagai kondisi(kemungkinan) beserta hasil ##