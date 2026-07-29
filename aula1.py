
faturamento=1200 # tipo: int--> numero inteiro
custo=750.0 # tipo float --> numero com casa decimal
novas_vendas=100
faturamento= faturamento + novas_vendas
imposto= faturamento * 0.1
lucro= faturamento- custo - imposto
margem_lucro=lucro/faturamento
print("O faturamento foi de ", faturamento)
print(" O custo foi de ",custo)
print(" o lucro foi de ",lucro)
print(" A margem de lucro foi de", round (margem_lucro,1))#arredondamento--> round(numero que vai arredondar , numeros de casas)
mensagem= "O Faturamento da loja foi de tanto"
email="emailqualquer@gmail.com" # tipo string --> texto
teve_lucro=True # variavel tipo boolean
#mod--> % resto da divisao
tempo_contrato= 170
tempo_anos=170/12
tempo_meses= 170%12
print("tempo em anos", int(tempo_anos))
print("tempo em meses ", tempo_meses)
