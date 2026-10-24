# =============================================================
# ZADATAK 4: PROJEKAT "To-do lista"
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
# Pravimo malu aplikaciju za listu obaveza koja radi u konzoli.
# Meni (DIO 2) je već napisan - pokreni fajl odmah i probaj ga!
# Opcije još ne rade, jer funkcije u DIJELU 1 nisu napisane.
#
#   NIVO 1: dodaj(), prikazi()             -> lista radi u memoriji
#   NIVO 2: oznaci_gotovo(), obrisi()      -> uređivanje liste
#   NIVO 3: sacuvaj(), ucitaj()            -> lista ostaje i nakon
#                                             zatvaranja programa
#   BONUS : statistika(), sortiraj_po_prioritetu()
#
# Pišeš SAMO u DIO 1. DIO 2 (meni) ne mijenjaj.
# =============================================================
import os

# =============================================================
# DIO 1: TVOJ KOD
# =============================================================
# Jedan zadatak je rječnik:
#   {"naziv": "Kupiti mlijeko", "gotovo": False, "prioritet": 2}
# Prioritet: 1 = visok, 2 = srednji, 3 = nizak
# Cijela lista je lista takvih rječnika.


# NIVO 1: Dodavanje i prikaz
# dodaj: ako je naziv prazan string, ispiši "Naziv ne može biti prazan."
#        i ništa ne dodaj. Inače dodaj novi rječnik na kraj liste
#        (gotovo = False).
def dodaj(zadaci, naziv, prioritet=2):
    if not naziv:
        print("Naziv ne može biti prazan.")
        return
    zadaci.append({"naziv": naziv, "gotovo": False, "prioritet": prioritet})


# prikazi: ako je lista prazna, ispiši "Lista je prazna."
#          Inače ispiši svaki zadatak u obliku:
#             1. [ ] Kupiti mlijeko  (prioritet: 2)
#             2. [x] Učiti Python  (prioritet: 1)
#          ([x] = gotovo, [ ] = nije gotovo)
# Savjet: for i, z in enumerate(zadaci, start=1):
def prikazi(zadaci):
    if not zadaci:
        print("Lista je prazna.")
        return

    for i, z in enumerate(zadaci, start=1):
        status = "x" if z["gotovo"] else " "
        print(f"{i}. [{status}] {z['naziv']}  (prioritet: {z['prioritet']})")


# NIVO 2: Označavanje i brisanje
# broj je redni broj sa ekrana (kreće od 1!), a indeks u listi od 0.
# Ako broj nije između 1 i len(zadaci): ispiši "Nepostojeći broj zadatka."
# i vrati False. Inače uradi posao i vrati True.
def oznaci_gotovo(zadaci, broj):
    if broj < 1 or broj > len(zadaci):
        print("Nepostojeći broj zadatka.")
        return False

    zadaci[broj - 1]["gotovo"] = True
    return True


# obrisi: ukloni zadatak sa liste (savjet: pop) i ispiši
#         "Obrisano: <naziv>"
def obrisi(zadaci, broj):
    if broj < 1 or broj > len(zadaci):
        print("Nepostojeći broj zadatka.")
        return False

    zadatak = zadaci.pop(broj - 1)
    print(f"Obrisano: {zadatak['naziv']}")
    return True


# NIVO 3: Čuvanje u fajl i učitavanje iz fajla
# Format jednog reda u fajlu:  gotovo;prioritet;naziv
#   npr.  0;2;Kupiti mlijeko      (gotovo: 1 = da, 0 = ne)
def sacuvaj(zadaci, fajl):
    with open(fajl, "w", encoding="utf-8") as f:
        for z in zadaci:
            gotovo = 1 if z["gotovo"] else 0
            f.write(f"{gotovo};{z['prioritet']};{z['naziv']}\n")


# ucitaj: vrati listu rječnika pročitanu iz fajla.
#   - ako fajl ne postoji (prvo pokretanje), vrati praznu listu
#     (savjet: os.path.exists(fajl))
#   - svaki red: strip(), pa red.split(";", 2)
#     (2 = najviše 3 dijela, pa naziv smije sadržavati ";")
#   - gotovo je True ako je u fajlu "1"; prioritet pretvori u int
def ucitaj(fajl):
    if not os.path.exists(fajl):
        return []

    zadaci = []
    with open(fajl, "r", encoding="utf-8") as f:
        for red in f:
            red = red.strip()
            if not red:
                continue
            gotovo, prioritet, naziv = red.split(";", 2)
            zadaci.append({
                "naziv": naziv,
                "gotovo": gotovo == "1",
                "prioritet": int(prioritet),
            })
    return zadaci


# BONUS 1: statistika vraća (ukupno, zavrseno, procenat)
#   - zavrseno izračunaj pomoću list comprehension-a
#   - procenat zaokruži na 1 decimalu; za praznu listu procenat = 0
def statistika(zadaci):
    ukupno = len(zadaci)
    zavrseno = len([z for z in zadaci if z["gotovo"]])
    procenat = round(zavrseno / ukupno * 100, 1) if ukupno else 0
    return ukupno, zavrseno, procenat


# BONUS 2: vrati NOVU listu sortiranu tako da su nezavršeni prvi,
#          a unutar toga po prioritetu (1, 2, 3).
# Savjet: sorted(zadaci, key=lambda z: (z["gotovo"], z["prioritet"]))
def sortiraj_po_prioritetu(zadaci):
    return sorted(zadaci, key=lambda z: (z["gotovo"], z["prioritet"]))


# =============================================================
# DIO 2: DATI KOD - meni aplikacije (ne mijenjaj)
# =============================================================
# Fajl todo.txt se čuva u istom folderu kao ova skripta
FAJL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todo.txt")

MENI = """
========== TO-DO LISTA ==========
1 - Dodaj zadatak
2 - Prikaži listu
3 - Označi kao gotovo
4 - Obriši zadatak
5 - Sortiraj po prioritetu
6 - Statistika
0 - Sačuvaj i izađi"""


def unesi_broj(poruka):
    """Traži cijeli broj od korisnika. Vraća None ako unos nije broj."""
    try:
        return int(input(poruka))
    except ValueError:
        print("Molim unesi broj.")
        return None


def main():
    zadaci = ucitaj(FAJL)
    print(f"Učitano zadataka iz fajla: {len(zadaci)}")

    while True:
        print(MENI)
        izbor = input("Izbor: ").strip()

        if izbor == "1":
            naziv = input("Naziv zadatka: ").strip()
            prioritet = unesi_broj("Prioritet (1 = visok, 2 = srednji, 3 = nizak): ")
            if prioritet not in (1, 2, 3):
                print("Prioritet postavljen na 2 (srednji).")
                prioritet = 2
            dodaj(zadaci, naziv, prioritet)

        elif izbor == "2":
            prikazi(zadaci)

        elif izbor == "3":
            prikazi(zadaci)
            broj = unesi_broj("Broj zadatka koji je gotov: ")
            if broj is not None and oznaci_gotovo(zadaci, broj):
                print("Zadatak označen kao gotov.")

        elif izbor == "4":
            prikazi(zadaci)
            broj = unesi_broj("Broj zadatka za brisanje: ")
            if broj is not None:
                obrisi(zadaci, broj)

        elif izbor == "5":
            zadaci = sortiraj_po_prioritetu(zadaci)
            prikazi(zadaci)

        elif izbor == "6":
            ukupno, zavrseno, procenat = statistika(zadaci)
            print(f"Ukupno: {ukupno} | Završeno: {zavrseno} | Urađeno: {procenat}%")

        elif izbor == "0":
            sacuvaj(zadaci, FAJL)
            print("Lista je sačuvana. Doviđenja!")
            break

        else:
            print("Nepoznata opcija, pokušaj ponovo.")


if __name__ == "__main__":
    main()
