# Surface Blasting Design Calculator

import math

rock = input("Rock type (hard, medium, soft, very soft): ").lower()
if rock == "hard":
    K = 0.70

elif rock == "medium":
    K = 0.45

elif rock == "soft":
    K = 0.30

elif rock == "very soft":
    K = 0.25

else:
    print("Invalid rock type.")
    exit()
print("Powder Factor (K) =", K, "kg/m³")
# Inputs 
BD= float(input("value of blasting diameter in mm ="))
P= float(input("value of average hole density ="))
# Assume we are using staggered pattern
SB= float(input("value of spacing to burden ratio ="))
BH= float(input("value of bench height in m ="))
# Assume its a hard rock (granite)

Mc=( P*BD**2)/1273
SL= (30*BD)/1000
Burden= math.sqrt((Mc*(BH-SL)/(SB*K*BH)))
Spacing = Burden
SD= (1/3)*Burden

Kact= ((BH-SD)*Mc)/(Burden*Spacing*BH)    
print(f"Stemming length = {SL:.2f}m")
print(f"Burden = {Burden:.2f}m")
print(f"Actual powder factor = {Kact:.2f}kg/m**3")

# Fragmentation Calculator

# Assume Hard rock (Granite)

rock = input("Rock type (hard, medium, soft, very soft): ").lower()
if rock == "hard":
    A = 10
    K = 0.70

elif rock == "medium":
    A = 8
    K = 0.45

elif rock == "soft":
    A = 6
    K = 0.30

elif rock == "very soft":
    A = 4
    K = 0.25

else:
    print("Invalid rock type.")
    exit()

print("Rock Factor (A) =", A)
print("Powder Factor (K) =", K, "kg/m³")
  
E = float(input("Relative Effective Energy of Explosive in kg = "))
p =float(input("Average In-Hole Density in g/cm**3 = "))
BH = float(input("Bench Height in m = "))
SL = float(input("Stemming Lenght in m ="))

Mc =( p*200**2)/1273
CL = BH - SL
Q = Mc*CL

X50 = A*(K**(-0.8))*(Q**(1/6))*((115/E)**(19/20))
print(f"Mean fragmentation = {X50:.2f}")


