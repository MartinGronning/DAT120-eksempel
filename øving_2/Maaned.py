tall_streng = input("Skriv inn et tall for en måned: ")
maaned = int(tall_streng)

if maaned < 1 or maaned > 12:
    print("Ugyldig måned.")
    reell_maaned = False
else:
    print("Gyldig måned.")
    reell_maaned = True
    
if reell_maaned == True:
    if maaned >= 3 and maaned <= 5:
        print("�
rstiden er vår.")
    elif maaned >=6 and maaned <= 8:
        print("�
rstiden er sommer.")
    elif maaned >= 9 and maaned <= 11:
        print("�
rstiden er høst.")
    elif maaned == 12 or maaned == 1 or 2:
        print("�
rstiden er vinter.")