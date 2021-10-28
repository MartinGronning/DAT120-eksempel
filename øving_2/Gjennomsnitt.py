tall = int(input("Skriv inn et positivt tall: "))
summen = 0
nummer_count = 0

while tall >= 0:
    summen += tall
    nummer_count += 1
    gjennomsnitt = summen/nummer_count
    print(f"Gjennomsnittet er {gjennomsnitt}")
    tall = int(input("Skriv inn et annet positivt tall: "))
print(f"Det endelige gjennomsnittet er {gjennomsnitt}")