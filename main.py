"""
Šis modulis realizuoja klasikinį žaidimą Nuliukai ir Kryžiukai (Tic Tac Toe).

Pagrindinis funkcionalumas:
- Leidžia dvem žaidėjams įvesti savo vardus.
- Leidžia dviem žaidėjams žaisti žaidimą paeiliui.
- Leidžia žaidimo metu nutraukti žaidimą.
- Tikrina žaidimo būseną: ar yra laimėtojas, ar lygiosios, ar tęsti žaidimą.
- Pabaigus žaidimą informuoja kiek kartų laimėjo kiekvienas žaidėjas.

Pagrindinės funkcijos naudojamos žaidime:
- `atvaizduoti_lentele(langeliai)`: Atvaizduoja žaidimo lentelę.
- `kas_eina(ejimas)`: Grąžina žaidėjo simbolį pagal ėjimą.
- `tikrinimas(langeliai)`: Tikrina ar yra laimėtojas.
- `ar_zaidziam(zaidejas1, zaidejas2, x_pergales, o_pergales)`: Tikrina ar žaidėjai nori tęsti žaidimą.

Autorius: Virgilijus Javtokas
Data: 2025-01-23
Pastaba: Šis modulis skirtas mokymuisi ir pramogai.
"""

from pagalbinis import (atvaizduoti_lentele,
                        kas_eina,
                        tikrinimas,
                        ar_zaidziam)

langeliai = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
             9: "9"}
ejimas = 1
ejimai = []
x_pergales = 0
o_pergales = 0

print("\nNULIUKŲ IR KRYŽIUKŲ ŽAIDIMAS")
print("----------------------------")
print("""Taisyklės:
Pirmas žaidėjas norėdamas padaryti ėjimą įveda skaičių, kuris žymi vietą lentelėje ir spaudžia ENTER.
Tada tą patį daro antras žaidėjas. Žaidimas tęsiasi kol vienas iš žaidėjų laimi, t.y. savo pasirinktu
simboliu užpildo arba eilutę, arba stulpelį, arba įstrižainę.
Jei norėsite bet kada žaidimo metu jį pabaigti - iveskite 'B'\n""")

zaidejas1 = input("Įveskite pirmo žaidėjo vardą: ")
print(f"Sveiki {zaidejas1}! Jūs pradėsite pirmas ir žaisite su 'X' ženkleliu.\n")
zaidejas2 = input("Įveskite antro žaidėjo vardą: ")
print(f"Sveiki {zaidejas2}! Jūs žaisite su '0' ženkleliu.\n")
print("PRADEDAM!\n")

atvaizduoti_lentele(langeliai)

while True:
    pasirinkimas = input("Pasirinkite vietą įvesdami ją žymintį skaičių (veskite 'B' jei norite išeiti iš žaidimo): ")
    if pasirinkimas == "B":
        break
    if pasirinkimas.isdigit():
        if int(pasirinkimas) in range(1, 10) and int(pasirinkimas) not in ejimai:
            langeliai[int(pasirinkimas)] = kas_eina(ejimas) #langeliui priskiriamas X arba O pagal tai kieno eile
            print("")
            atvaizduoti_lentele(langeliai)
            ejimas += 1
            if int(pasirinkimas) not in ejimai:
                ejimai.append(int(pasirinkimas))
            if tikrinimas(langeliai):
                if langeliai[int(pasirinkimas)] == "X":
                    x_pergales += 1
                    print(f"Laimejo {zaidejas1}!")
                elif langeliai[int(pasirinkimas)] == "0":
                    o_pergales += 1
                    print(f"Laimejo {zaidejas2}!")
                ejimas, ejimai, langeliai = ar_zaidziam(zaidejas1, zaidejas2, x_pergales, o_pergales)

            elif len(ejimai) == 9:
                print("Lygiosios")
                ejimas, ejimai, langeliai = ar_zaidziam(zaidejas1, zaidejas2, x_pergales, o_pergales)
        else:
            print("Įvedėte neteisingą ėjimą - bandykite dar kartą.")
    else:
        print("Įvedėte neteisingą ėjimą - bandykite dar kartą")
