faturamento=1000
custo=200
lucro=faturamento-custo
margem_lucro=lucro/faturamento
print(f"faturamento da empresa:{faturamento},custo:{custo},lucro:{lucro}, margem de lucro{margem_lucro}")
email_cliente="qualquerl@gmail.com"
email_cliente=email_cliente.upper()#maíuscula
print(email_cliente)
email_cliente=email_cliente.lower()#míniscula
print(email_cliente)
#"@"
print(email_cliente.find("@"))#-1 quando nao encontrar
print(len(email_cliente)) #tamanho do texto
print(email_cliente[9:16])#pega um pedaço do texto
novo_email=email_cliente.replace("gmail.com","hotgmail.com")#troca um pedaço do texto
print(novo_email)

nome="gustavo henrique"
#trabalhar com nomes
print(nome.capitalize())
print(nome.title())

#pegar o servidor do email
posicao_arroba=email_cliente.find("@")+ 1
servidor=email_cliente[posicao_arroba:]
print(servidor)
#pegar o 1º nome
posicao_espaco=nome.find(" ")
primeiro_nome=nome[:posicao_espaco]
sobrenome=nome[posicao_espaco+1:]
print(primeiro_nome)
print(sobrenome)


#casos especias-formatações numéricas em texto
margem_lucro=round(margem_lucro, 2)
print(f"faturamento da empresa:${faturamento:.2f},custo:${custo:.2f},lucro:${lucro:.2f}, margem de lucro:${margem_lucro: .0%}")