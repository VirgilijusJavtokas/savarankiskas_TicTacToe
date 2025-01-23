"""
Šiame faile yra aprašyti pagalbiniai metodai, kurie atvaizduoja žaidimo
lentelę, priskiria simbolį pagal tai kas atlieka ėjimą, tikrina ar yra
laimėtojas ir ar žaidėjai nori tęsti žaidimą.
"""

import sys


def atvaizduoti_lentele(langeliai):
    '''
    Funkcija atvaizduoja žaidimo lentelę.
    :param langeliai: pradžioje žaidimo laukai nuo 1 iki 9, o po to keičiami
    pagal atitinkamo žaidėjo ėjimą.
    '''
    lentele = (f" {langeliai[1]} | {langeliai[2]} | {langeliai[3]} \n-----------\n"
               f" {langeliai[4]} | {langeliai[5]} | {langeliai[6]} \n-----------\n "
               f"{langeliai[7]} | {langeliai[8]} | {langeliai[9]} ")
    print(lentele)


def kas_eina(ejimas):
    '''
    Funkcija priskiria kas atlieka ėjimą. Pirmas ir tolimesni nelyginiai ėjimai
    yra žaidėjo kuris žaidžia X, o antras ir kiti lyginiai - žaidėjo, kuris
    žaidžia 0.
    :param ejimas: ėjimai nuo 1 iki max. 9
    :return: X arba 0 priklausomai koks žaidėjas daro ėjimą.
    '''
    if ejimas % 2 == 0:
        return "0"
    return "X"


def tikrinimas(langeliai):
    """
    Funkcija tikrina ar kuris nors iš žaidėjų laimėjo, t.y. patikrina ar nėra
    užbrauktos eilutės, stulpeliai ar įstrižainės
    :param langeliai: ima langelius iš lentelės po kiekvieno ėjimo
    :return: ar yra laimėjimas, ar nėra laimėjimo
    """
    if (langeliai[1] == langeliai[2] == langeliai[3] or langeliai[4] == langeliai[5] == langeliai[6] or \
            langeliai[7] == langeliai[8] == langeliai[9]):
        return True

    if (langeliai[1] == langeliai[4] == langeliai[7] or langeliai[2] == langeliai[5] == langeliai[8] or
            langeliai[3] == langeliai[6] == langeliai[9]):
        return True

    if (langeliai[1] == langeliai[5] == langeliai[9] or langeliai[7] == langeliai[5] == langeliai[3]):
        return True
    return False


def ar_zaidziam(zaidejas1, zaidejas2, x_pergales, o_pergales):
    """
    Funkcija tikrina kokį pasirinkimą padarė žaidėjas
    :param zaidejas1: pirmo žaidėjo vardas, kurį jis įvedė
    :param zaidejas2: antro žaidėjo vardas, kurį jis įvedė
    :param x_pergales: pirmo žaidėjo, kuris žaidžia X'u pergalės
    :param o_pergales: antro žaidėjo, kuris žaidžia 0'u pergalės
    :return: pasirinkus tęsti žaidima gražina atnaujintą ėjimo numerį, tuščią
    ėjimų sąrašą ir atnaujintą lentelę paruoštą naujam žaidimui
    """
    while True:
        arzaidziam = input("Ar norite žaisti dar kartą? (T/N): \n")
        if arzaidziam == "T":
            langeliai = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
            print("")
            print("Naujas žaidimas prasideda!")
            atvaizduoti_lentele(langeliai)
            ejimas = 1
            ejimai = []
            break
        if arzaidziam == "N":
            sys.exit(f"Žaidimas baigtas. {zaidejas1} pergalės: {x_pergales}, {zaidejas2} pergalės: {o_pergales}")
        else:
            print("Įvedėte negalimą pasirinkimą - bandykite dar kartą.")
    return ejimas, ejimai, langeliai
