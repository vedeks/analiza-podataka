import os
import random

studenti = ["Amra", "Emir", "Lejla", "Tarik", "Ana"]
bodovi = [78, 92, 65, 88, 92]

parovi = list(zip(studenti, bodovi))
for ime, broj_bodova in parovi:
    print(f"{ime}: {broj_bodova}")


rang_lista = sorted(parovi, key=lambda par: par[1], reverse=True)
for rang, (ime, broj_bodova) in enumerate(rang_lista, start=1):
    print(f"{rang}. {ime} - {broj_bodova}")

uspjesni = [ime for ime, broj_bodova in parovi if broj_bodova >= 80]
print(uspjesni)

FAJL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_birthdays.txt")
with open(FAJL, "r", encoding="utf-8") as f:
    mjeseci = [int(red.strip().split("-")[1]) for red in f if red.strip()]

print(sorted(set(mjeseci)))

random.seed(42)
student_koji_odgovara = random.choice(studenti)
redoslijed_prezentacija = studenti.copy()
random.shuffle(redoslijed_prezentacija)

print(f"Student koji odgovara: {student_koji_odgovara}")
print(f"Redoslijed prezentacija: {redoslijed_prezentacija}")
