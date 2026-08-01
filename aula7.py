lista_precos=[1500,1000,800,3000]

# imposto
# aliquota1 - IR = 0.2 , se o preço do produto for até de 2000 , acima disso a aliquota é 0.3
# aliquota2 - ISS = 0.15
# aliquota3 - CSLL = 0.05

def calcula_imposto_total(preco):
 if preco <=2000:
        imposto_ir=preco*0.2
 else:
        imposto_ir=preco*0.3
 imposto_iss=preco*0.15
 imposto_csll=preco*0.05
 imposto_total= imposto_ir+imposto_iss +imposto_csll
 return imposto_total



for preco in lista_precos:
    imposto_total= calcula_imposto_total(preco)
    print(f"Imposto total sobre o produto de R${preco}: é R${imposto_total}")
  

nova_lista_produtos=[3000,5000,6000,7000]

for preco in nova_lista_produtos:
 imposto_total=calcula_imposto_total(preco)
 print(f"Imposto total sobre o produto de R${preco}: é R${imposto_total}")
    