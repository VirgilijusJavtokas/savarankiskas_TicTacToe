from pagalbinis import atvaizduoti_lentele, kas_eina, tikrinimas, ar_zaidziam

langeliai = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
ejimas = 1
ejimai = []
x_pergales = 0
o_pergales = 0

print("\nNULIUKŲ IR KRYŽIUKŲ ŽAIDIMAS")
print("----------------------------")
print("""Taisyklės: 
Pirmas žaidėjas norėdamas padaryti ėjimą įveda skaičių, kuris žymi vietą lentelėje ir spaudžia ENTER.
Tada tą patį daro antras žaidėjas. Žaidimas tęsiasi kol vienas iš žaidėjų laimi.
Jei norėsitte bet kada žaidimo metu jį pabaigti - iveskite 'B'\n""")

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
    else:
        if pasirinkimas.isdigit():
            if int(pasirinkimas) in range(1, 10) and int(pasirinkimas) not in ejimai:
                langeliai[int(pasirinkimas)] = kas_eina(ejimas)
                print("")
                atvaizduoti_lentele(langeliai)
                ejimas += 1
                if int(pasirinkimas) not in ejimai: ejimai.append(int(pasirinkimas))
                if tikrinimas(langeliai) == True:
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

