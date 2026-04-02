numbers = []
sum_all = 0.0

while True:
    user_input = input("Unesi broj ili 'done' za prekid: ")

    if user_input.lower() == "done":
        break

    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Greška: uneseni podatak nije broj.")

if not numbers:
    print("Nema unesenih brojeva – ne možemo računati prosjek.")
else:
    sum_all = sum(numbers)
    print(f"Broj unesenih vrijednosti: {len(numbers)}")
    print(f"Prosjek: {sum_all / len(numbers):.2f}")
    print(f"Minimalna vrijednost: {min(numbers)}")
    print(f"Maksimalna vrijednost: {max(numbers)}")