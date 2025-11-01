#Name : Moosa Shehzad Abbasi
#U-number : U37033529
#Brief description : Area of composite shape

p = float(input('Enter the first diagonal length:'))
q = float(input('Enter the second diagonal length:'))
r = float(input('Enter the third diagonal length:'))
pi = 3.141592653589793
area = ((p * q)/2)-(pi * r**2)
format_area = "{:.3f}".format(area)

print('Area is:',format_area)
