def atvaizduoti_lentele(langeliai):
    lentele = (f" {langeliai[1]} | {langeliai[2]} | {langeliai[3]} \n-----------\n"
               f" {langeliai[4]} | {langeliai[5]} | {langeliai[6]} \n-----------\n "
               f"{langeliai[7]} | {langeliai[8]} | {langeliai[9]} ")
    print(lentele)


def kas_eina(ejimas):  # tikrina kieno ejimas
    if ejimas % 2 == 0:
        return "0"
    else:
        return "X"


def tikrinimas(langeliai):  # tikrina ar laimejo
    # tikrina eilutes del laimejimo
    if (langeliai[1] == langeliai[2] == langeliai[3] or langeliai[4] == langeliai[5] == langeliai[6] or \
            langeliai[7] == langeliai[8] == langeliai[9]):
        return True
    # tikrina stulpelius del laimejimo
    elif (langeliai[1] == langeliai[4] == langeliai[7] or langeliai[2] == langeliai[5] == langeliai[8] or \
          langeliai[3] == langeliai[6] == langeliai[9]):
        return True
        # tikrina istrizaines del laimejimo
    elif (langeliai[1] == langeliai[5] == langeliai[9] or langeliai[7] == langeliai[5] == langeliai[3]):
        return True
    else:
        return False


def ar_zaidziam(zaidejas1, zaidejas2, x_pergales, o_pergales):
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
