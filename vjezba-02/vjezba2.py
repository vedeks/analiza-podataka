import os
from collections import Counter


FAJL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_birthdays.txt")

with open(FAJL, "r", encoding="utf-8") as f:
    datumi = [red.strip() for red in f if red.strip()]

ukupno = len(datumi)
jedinstveni = set(datumi)
brojac = Counter(datumi)
ponavljanja = sorted((datum, broj) for datum, broj in brojac.items() if broj > 1)

print(f"Ukupno rođendana: {ukupno}")
print(f"Jedinstvenih rođendana: {len(jedinstveni)}")
print(f"Postoje li duplikati: {bool(ponavljanja)}")
print("Datumi koji se ponavljaju:")
for datum, broj in ponavljanja:
    print(f"{datum} -> {broj} puta")


def vjerovatnoca_poklapanja(n):
    if n <= 1:
        return 0.0
    if n > 365:
        return 1.0

    vjerovatnoca_bez_poklapanja = 1.0
    for osoba in range(n):
        vjerovatnoca_bez_poklapanja *= (365 - osoba) / 365
    return 1 - vjerovatnoca_bez_poklapanja


vjerovatnoca = vjerovatnoca_poklapanja(38)
print(f"Teorijska vjerovatnoća za 38 osoba: {vjerovatnoca:.1%}")
if ponavljanja:
    print("U podacima postoji poklapanje, što je u skladu s visokom teorijskom vjerovatnoćom.")
else:
    print("U podacima nema poklapanja, iako je ono teorijski vjerovatno.")
