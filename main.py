# from lentele import atvaizduoti_lentele
def atvaizduoti_lentele(langeliai):
    lentele = (f" {langeliai[1]} | {langeliai[2]} | {langeliai[3]} \n-----------\n"
               f" {langeliai[4]} | {langeliai[5]} | {langeliai[6]} \n-----------\n "
               f"{langeliai[7]} | {langeliai[8]} | {langeliai[9]} ")
    print(lentele)

def kas_eina(ejimas):
    if ejimas % 2 == 0:
        return "0"
    else:
        return "X"

def tikrinimas(dict):
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

zaidimas = True
ejimas = 1
langeliai = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9"}
x_pergales = 0
o_pergales = 0

print("\nNULIUKŲ IR KRYŽIUKŲ ŽAIDIMAS")
print("----------------------------")
print("""Taisyklės: 
Pirmas žaidėjas žaidžia 'X', o antras '0'. 
Žaidėjas įveda skaičių, kuris žymi vietą lentelėje.
Jei norite pabaigti žaidimą - iveskite 'N'
PRADEDAM !\n""")
atvaizduoti_lentele(langeliai)
ejimai = []

while True:
    pasirinkimas = input("Pasirinkite vieta ivesdami ja zyminti skaiciu (veskite 'B' jei norite iseiti is zaidimo): ")
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
                    break
            else:
                print("Ivedete neteisinga ejima - bandykite dar karta.")
        else:
            print("Ivedete neteisinga ejima - bandykite dar karta.")

#