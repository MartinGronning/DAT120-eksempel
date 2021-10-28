tall = int(input("Skriv inn et positivt heltall: "))
summen = 0

while tall >= 0:
    summen += tall
    print(f"Summen er {summen}")
    tall = int(input("Skriv inn et annet positivt heltall: "))
print(f"Den endelige summen er {summen}")