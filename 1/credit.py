#20000*(1+15/(12*100))**(5*12)
import decimal
sum=int(input("Введите вашу сумму: "))
per=int(input('Введите срок в годах: '))
proc=float(input("Введите процент: "))
all_sum=decimal.Decimal(sum*((1+proc/(12*100))**(per*12)))
print(decimal.Decimal(all_sum))