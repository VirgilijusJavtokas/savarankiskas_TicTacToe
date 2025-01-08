# Pradžioje planavau naudoti daugiau failu, tad lenteles atvaizdavimo funkciją buvau padaręs atskiramefaile, bet
# nusprendžiau viską sudėti į vieną failą, todėl liko failas lentele.py nepanaudotas ir sekanti import komanda
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
    #tikrina eilutes
    if (langeliai[1] == langeliai[2] == langeliai[3] or langeliai[4] == langeliai[5] == langeliai[6] or \
            langeliai[7] == langeliai[8] == langeliai[9]):
        return  True
    # tikrina stulpelius
    elif (langeliai[1] == langeliai[4] == langeliai[5] or langeliai[2] == langeliai[5] == langeliai[8] or \
        langeliai[3] == langeliai[6] == langeliai[9]):
        return True
        # tikrina istrizaines
    elif (langeliai[1] == langeliai[5] == langeliai[9] or langeliai[7] == langeliai[5] == langeliai[3]):
        return True
    else: return False


langeliai = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9"}
ejimas = 1
ejimai = []
x_pergales = 0
o_pergales = 0

print("\nNULIUKŲ IR KRYŽIUKŲ ŽAIDIMAS")
print("----------------------------")
print("""Taisyklės: 
Pirmas žaidėjas žaidžia 'X', o antras '0'. 
Žaidėjas įveda skaičių, kuris žymi vietą lentelėje.
Jei norite bet kada pabaigti žaidimą - iveskite 'B'
PRADEDAM !\n""")

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
                    print(f"Laimejo {langeliai[int(pasirinkimas)]} zaidejas")
                    if langeliai[int(pasirinkimas)] == "X": x_pergales += 1
                    elif langeliai[int(pasirinkimas)] == "0": o_pergales += 1
                    # zaidimas = False
                    arzaidziam = input("Ar norite zaisti dar karta? (T/N): ")
                    if arzaidziam == "T":
                        langeliai = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
                        atvaizduoti_lentele(langeliai)
                        ejimas = 1
                        ejimai = []
                    else:
                        print(f"Žaidimas baigtas. 'X' žaidėjo pergalės: {x_pergales}, 'O' žaidėjo pergalės: {o_pergales}")
                        break
            else:
                print("Įvedėte neteisingą ėjimą - bandykite dar kartą.")
        else:
            print("Įvedėte neteisingą ėjimą - bandykite dar kartą")
#