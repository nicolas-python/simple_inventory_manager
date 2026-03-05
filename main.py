#simple_inventory_manager
                #lager
lager = {
        "obst": ["Apfel", "Trauben","Bannanen"],
        "gemuese": ["Karotte","Zucchini","Salat"],
        "suesigkeiten": ["Lolis","Chips"]
    }

                                    #menü
def simple_inventory_manager():
    choice = None

    while choice not in ["1","2","3","4"]:
        print("Python Inventory Manager")
        print("1 = Product hinzufügen")
        print("2 = Produkt Anzeigen")
        print("3 = Produkt Löschen")
        print("4 = Beenden")

        choice = input("Wähle eine Option:")

        if choice not in ["1","2","3","4"]:
            print("Ungültige Option, bitte erneut wählen.")

    return choice



#Prudukt hinzfuegen

def product_hinzufuegen():

        category = input("Kategorie wählen: obst,gemuese,suesigkeiten: ")
        product = input("Produkt eingeben :")

        if category in lager :
            lager[category].append(product)
            print("Product wurde zum lager hinzugefügt")

        else:
            print("Kategorie nicht gefunden")



#Produkte anzeigen

def product_anzeigen():

        category = input("Kategorie wählen: obst,gemüse,suesigkeiten: ")
        if category in lager :
            print(lager[category])
        else :
            print("Kategorie nicht gefunden")



#Produkte löschen

def product_loeschen():

    category = input("Kategorie wählen: obst,gemuese,suesigkeiten: ")
    product = input("Produkt eingeben :")

    if category in lager:

        try:
            lager[category].remove(product)
            print("Product wurde aus dem lager entfernt")
        except NameError:
            print("Produkt nicht gefunden")

    else:
        print("Kategorie nicht gefunden")

#Funktion abrufen
choice = simple_inventory_manager()

if choice == "1":
    product_hinzufuegen()

if choice == "2":
    product_anzeigen()

if choice == "3":
    product_loeschen()

