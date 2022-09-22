#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#		              Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def valor_fruta(morango):
 if morango > 5:
    morango = morango * 2.20
    return morango
 elif morango <= 5:
     morango = morango * 2.50 
     return morango
def valormaca(maca):
 if maca <= 5:
   maca = maca * 1.80
   return maca
 elif maca > 5:
  maca = maca * 1.50
  return maca

morango = float(input("Informe quantos Kg deseja comprar de morango: "))
maca = float(input("Informe quantos Kg deseja comprar de maçã: "))
valormorango = valor_fruta(morango)
valormaca = valormaca(maca)
totalkg = morango + maca
somafruta = valormorango + valormaca
if somafruta > 25:
   somafruta = somafruta - somafruta * (10/100)
   print("O valor a pagar será de:", somafruta) 
elif totalkg > 8:             
  print("O valor a ser pago, será de: R$ ", somafruta - somafruta *  (10/100))