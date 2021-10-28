tall_streng = input("Skriv inn et tall for en mÃ¥ned: ")
maaned = int(tall_streng)

if maaned < 1 or maaned > 12:
    print("Ugyldig mÃ¥ned.")
    reell_maaned = False
else:
    print("Gyldig mÃ¥ned.")
    reell_maaned = True
    
if reell_maaned == True:
    if maaned >= 3 and maaned <= 5:
        print("Ã
rstiden er vÃ¥r.")
    elif maaned >=6 and maaned <= 8:
        print("Ã
rstiden er sommer.")
    elif maaned >= 9 and maaned <= 11:
        print("Ã
rstiden er hÃ¸st.")
    elif maaned == 12 or maaned == 1 or 2:
        print("Ã
rstiden er vinter.")