#inputs
#email=input("Escreva seu e-mail: ")
#nome=input("Seu primeiro nome: ")
#print(nome,email)
#print(f"{nome},verifique seu email: {email} que enviamos um link de confirmaçao")
#faturamento=float (input("Escreva o faturamento"))
#imposto=faturamento*0.1
#print(imposto)
  
 #listas
vendas=[100,50,14,20,30,700]

#soma das listas
total_vendas=sum(vendas)
print(total_vendas)

#tamanho da lista
quantidade_vendas=len(vendas)
print(quantidade_vendas)

#max e min
print (max(vendas))
print(min(vendas))

#pegar posicao
print(vendas[0])


listas_produtos=["iphone","android","ipad","macbook"]
#produto_procurado=input("Pesquise pelo nome do produto ")
#produto_procurado=produto_procurado.lower()
#print(produto_procurado in listas_produtos)

#adicionar um item
listas_produtos.append("apple watch")
print(listas_produtos)


#remover item
listas_produtos.remove("apple watch")
print(listas_produtos)


listas_produtos.pop(0)
print(listas_produtos)

#editar item
precos=[1000,1500,3500]
precos[0]=precos[0] *1.5
print(precos)

#contar quantas vezes um item aparece na lista
listas_produtos=["iphone","android","ipad","macbook","iphone"]


print(listas_produtos.count("iphone"))

 #ordenar uma lista
listas_produtos.sort()
print(listas_produtos)
listas_produtos.sort(reverse=True)
print(listas_produtos)