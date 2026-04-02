try:

    number = float(input("Unesi ocjenu: "))

    if number > 1.0 or number < 0.0:
        print("Ocjena nije u intervalu")
    elif number >= 0.9:
        print("A")
    elif number >= 0.8:
        print("B")
    elif number >= 0.7:
        print("C")
    elif number >= 0.6:
        print("D")
    else:
        print("F")

except:
    print("Unesite broj, a ne slovo!.")
