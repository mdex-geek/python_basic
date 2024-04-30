import math

def circlestats(radius):
   area= math.pi*radius**2
   circumference = 2*math.pi*radius
   return round(area) , round(circumference)

a,c =circlestats(10)
 
print("Area:",a,"\ncircumference:",c)

