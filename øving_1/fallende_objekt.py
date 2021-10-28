"""

@author: Martin Grønningen

"""
starttid = 0
startfart = 0
g = 9.81

sekunder_falt_str = input("Hvor lenge har objektet falt i sekunder?\n")

tid = int(sekunder_falt_str)

fart = g * tid
distanse = 0.5 * fart * tid
dist = round(distanse,2)

print("Farten er: ",round(fart,2),"m/s\nog\nDistansen er: ",round(distanse,2),"m",sep = '')