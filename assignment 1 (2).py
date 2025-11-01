#NAME : Moosa Shehzad Abbasi
#U number: U37033529
#Brief description: Newtons Law Of Universal Gravitation
## All the values used in the program are from byjus.com

G = 6.67e-11         #G is gravitational constant
M1 = 1.99e30         #M1 is the mass of sun
M2 = 5.97e24         #M2 is the mass of earth 


M3 = 7.34e24         #M3 is the mass of moon
D1 = 1.504e11        #D1 is the distance between sun and earth
D2= 3.84e8           #D2 is the distance between earth and moon
D3 = 1.47e11         #D3 is the distance between sun and moon


F1 = (G * M1 * M3)/D3**2           #F1 is the force exerted by sun on moon ==This is the ans to the a) part
print('The force F1 is: ',F1)

F2 = (G * M2 * M3)/D2**2           #F2 is the force exerted by earth on moon== This is the ans to the b) part
print('The force F2 is: ',F2)

F3 = (G * M1 * M2)/D1**2           #F3 is the force exerted by Sun on earth==This is the ans to the c) part
print('The force F3 is: ',F3)
