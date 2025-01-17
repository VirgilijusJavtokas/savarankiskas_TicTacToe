# Pradžioje planavau naudoti daugiau failu, tad lenteles atvaizdavimo funkciją buvau padaręs atskirame faile, bet
# nusprendžiau viską sudėti į vieną failą, todėl liko failas lentele.py nepanaudotas ir todel sekanti import komanda
# užkomentuota.

# from lentele import atvaizduoti_lentele

def atvaizduoti_lentele(langeliai):
    lentele = (f" {langeliai[1]} | {langeliai[2]} | {langeliai[3]} \n-----------\n"
               f" {langeliai[4]} | {langeliai[5]} | {langeliai[6]} \n-----------\n "
               f"{langeliai[7]} | {langeliai[8]} | {langeliai[9]} ")
    print(lentele)

def kas_eina(ejimas): #tikrina kieno ejimas
    if ejimas % 2 == 0:
        return "0"
    else:
        return "X"

def tikrinimas(dict): #tikrina ar laimejo
    #tikrina eilutes del laimejimo
    if (langeliai[1] == langeliai[2] == langeliai[3] or langeliai[4] == langeliai[5] == langeliai[6] or \
            langeliai[7] == langeliai[8] == langeliai[9]):
        return  True
    # tikrina stulpelius del laimejimo
    elif (langeliai[1] == langeliai[4] == langeliai[7] or langeliai[2] == langeliai[5] == langeliai[8] or \
        langeliai[3] == langeliai[6] == langeliai[9]):
        return True
        # tikrina istrizaines del laimejimo
    elif (langeliai[1] == langeliai[5] == langeliai[9] or langeliai[7] == langeliai[5] == langeliai[3]):
        return True
    else: return False

def ar_zaidziam():
    while True:
        arzaidziam = input("Ar norite zaisti dar karta? (T/N): \n")
        if arzaidziam == "T":
            langeliai = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
            atvaizduoti_lentele(langeliai)
            ejimas = 1
            ejimai = []
            print("Naujas žaidimas prasideda!")
            break
        elif arzaidziam == "N":
            quit(
                f"Žaidimas baigtas. {zaidejas1} pergalės: {x_pergales}, {zaidejas2} pergalės: {o_pergales}")
        else:
            print("Įvedėte neteisingą ėjimą - bandykite dar kartą.")
    return ejimas, ejimai, langeliai

langeliai = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9"}
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
print(f"Sveiki {zaidejas1}! Jūs pradėsite pirmas ir žaisite su 'X' ženkleliu.")
zaidejas2 = input("Įveskite antro žaidėjo vardą: ")
print(f"Sveiki {zaidejas2}! Jūs žaisite su '0' ženkleliu.\n")
print("PRADEDAM!\n")

atvaizduoti_lentele(langeliai)

while True:
    pasirinkimas = input("Pasirinkite vietą įvesdami ją žymintį skaičių (veskite 'B' jei norite išeiti iš žaidimo): ")
    if pasirinkimas == "B": break
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
                    ejimas, ejimai, langeliai = ar_zaidziam()

                elif len(ejimai) == 9:
                    print("Lygiosios")
                    ejimas, ejimai, langeliai = ar_zaidziam()
            else:
                print("Įvedėte neteisingą ėjimą - bandykite dar kartą.")
        else:
            print("Įvedėte neteisingą ėjimą - bandykite dar kartą")
