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

zaidimas = True
ejimas = 1
langeliai = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9"}

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
            if int(pasirinkimas) in range(1, 9) and int(pasirinkimas) not in ejimai:
                langeliai[int(pasirinkimas)] = kas_eina(ejimas)
                print("")
                atvaizduoti_lentele(langeliai)
                ejimas += 1
                ejimai.append(int(pasirinkimas))
            else:
                print("Ivedete neteisinga ejima - bandykite dar karta.")
        else:
            print("Ivedete neteisinga ejima - bandykite dar karta.")