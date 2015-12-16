## Loan and Payment Calculator V.1

print("Cliff's Loan Payment Calculator V.1")
print('Enter amount borrowed:')
dollaramount = int(input('$',))
centsamount = dollaramount * 100

print('Enter annual interest rate:')
aprsimp = float(input('%',))
apr = aprsimp / 100

print('Enter term in years:')
years = int(input())

interest = round((apr * years * centsamount) / 100, 2)
totowed = interest + dollaramount

print(' ')
print(' ')
print('*'.center(36,'*'))
print(' LOAN DETAILS '.center(36,'*'))
print('*'.center(36,'*'))

print('Principle             $',dollaramount)  
print('Interest              $',interest)
print('Total Amount Owed     $',totowed)

amtpaid = 0
rembal = totowed 
amtpaidtot = 0
months = years * 12
i = 1

print(' ')
print(' ')
print('*'.center(36,'*'))
print(' PAYMENT SCHEDULE '.center(36,'*'))
print('*'.center(36,'*'))
      
print('Month'.center(5),'Payment'.center(20),'Balance'.center(5))
print('-'.center(36,'-'))
for i in range(months + 1):
        print(str(i).center(5),str(round(amtpaid, 2)).center(20),str(abs(round(rembal, 2))).center(5))
        amtpaid = totowed / months 
        amtpaidtot = amtpaidtot + amtpaid 
        rembal = rembal - amtpaid
        i = i+1
        
input('press any key to exit')
