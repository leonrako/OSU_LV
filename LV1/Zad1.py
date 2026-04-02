def total_euro(hours, paid):
    return hours*paid

hours = float(input("Radni sati: "))
paid = float(input("eura/h: "))

print(f"Ukupno {total_euro(hours, paid)}")
