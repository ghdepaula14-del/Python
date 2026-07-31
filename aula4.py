vendas=1500
meta=1300

# > maior que 
# < menor que
# >= maior ou igual
# <= menor ou igual
# == igual
# != diferente
  
if vendas > meta:
    print("Vendedor ganha bônus")
    print("bateu a meta de vendas")
    bonus= 0.1 * vendas
    print("Bônus do vendedor",bonus)
else:
    print("Vendedor não ganha bônus")
    print("Nâo bateu a meta de vendas")

print("Acabou o programa!")

# 2º cenário
 
vendas=2000
vendas_empresa= 220000
meta1=1300 #ganhar 10%
meta2=2000 #ganhar 13%
meta_empresa=20000
if vendas >= 2000 and vendas_empresa >= meta_empresa:
    bonus =  0.13* vendas
elif vendas >= 2000 and vendas_empresa >=meta_empresa: #quantos quiser 
    bonus =  0.1* vendas
else:
    bonus=0
print("bônus:", bonus)

listas_produtos=["iphone","android","ipad","macbook","iphone"]
produto_procurado=input("Procure um produto:")
produto_procurado=produto_procurado.lower()

if produto_procurado in listas_produtos:
    print("produto no estoque")
else:
    print("produto não encotrado")

    
