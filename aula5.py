listas_vendas=[1000,500,800,2000,2300]
meta=100
percentual_bônus=0.1
venda=1000
for venda in listas_vendas:
 if venda >= meta:
    bonus=percentual_bônus*venda
 else:
    bonus=0


 print ( "Seu bõnus é de:",bonus)
#for venda in listas_vendas:
 #print(venda)
# print("proximo item")

#fora do for