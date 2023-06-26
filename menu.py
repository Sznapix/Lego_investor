import main
while True:
    print("""
            Menu porównywarki cenowej lego 
            
            1.Pobranie ofert i dodanie do bazy danych
            2.Wyświetlenie wszystkich ofert z bazy danych
            3.Wyświetlenie najabrdziej opłacalnych ofert do zkaupu i sprzedaży
            4.Wyczyszczenie bazy danych 
            5.zamkniecie programu
    """)
    choice = str(input("Podaj swój wybór"))
    match choice:
        case "1":
            main.adding_to_database()
        case "2":
            main.print_all_values_in_database()
        case "3":
            main.the_best_offer()
        case "4":
            warning = input("Czy na pewno chcesz wyczyścić baze danych? Jeśli tak napisz TAK: ")
            if warning == "TAK":
                main.clear_database()
            else:
                pass
        case "5":
            break
        case _ :
            print("Nie podałeś zadnej opcji lub podałeś błędną podaj ją jeszcze raz")
