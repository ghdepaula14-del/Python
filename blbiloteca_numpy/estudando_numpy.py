
# Importa a biblioteca NumPy e dá a ela o apelido "np"
import numpy as np

# Importa a biblioteca time
# (Ainda não está sendo utilizada neste código)
import time

# Importa o gerador moderno de números aleatórios do NumPy
from numpy.random import default_rng


# ============================================================
# 1. CRIANDO ARRAYS
# ============================================================

# Cria um array bidimensional (2 linhas e 6 colunas)
a = np.array([
    [1, 2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7, 8]
])

# Mostra o array
print("Array A:")
print(a)

# Mostra o tipo da variável
print("\nTipo do array:")
print(type(a))


# ============================================================
# 2. CRIANDO ARRAYS DE ZEROS
# ============================================================

# Cria um array de zeros com:
# 5 blocos
# 3 linhas
# 6 colunas
zero_array = np.zeros(shape=(5, 3, 6))

print("\nArray de zeros:")
print(zero_array)


# ============================================================
# 3. CRIANDO ARRAYS DE UNS
# ============================================================

# Cria um array de uns com:
# 2 linhas
# 3 colunas
um_array = np.ones(shape=(2, 3))

print("\nArray de uns:")
print(um_array)


# ============================================================
# 4. CRIANDO UM ARRAY VAZIO
# ============================================================

# Cria um array vazio com 3 linhas e 4 colunas
# ATENÇÃO:
# np.empty() não coloca zeros.
# Os valores que aparecem podem ser qualquer coisa que estava
# anteriormente na memória do computador.
vazio = np.empty((3, 4))

print("\nArray vazio:")
print(vazio)


# ============================================================
# 5. CRIANDO SEQUÊNCIAS COM ARANGE
# ============================================================

# Cria números de 50 até antes de 200,
# pulando de 30 em 30
arr = np.arange(50, 200, 30)

print("\nArray criado com arange:")
print(arr)


# ============================================================
# 6. CRIANDO NÚMEROS ESPAÇADOS COM LINSPACE
# ============================================================

# Cria 40 números igualmente espaçados entre 0 e 100
# retstep=True também mostra o intervalo entre os números
array_linear = np.linspace(
    0,
    100,
    num=40,
    retstep=True
)

print("\nArray criado com linspace:")
print(array_linear)


# ============================================================
# 7. INFORMAÇÕES SOBRE UM ARRAY
# ============================================================

# shape mostra o formato do array
print("\nFormato do zero_array:")
print(zero_array.shape)

# size mostra a quantidade total de elementos
print("\nQuantidade de elementos:")
print(zero_array.size)

# ndim mostra a quantidade de dimensões
print("\nQuantidade de dimensões:")
print(zero_array.ndim)


# ============================================================
# 8. ARRAYS DE 1 DIMENSÃO
# ============================================================

# Cria um array de uma dimensão
b = np.array([1, 2, 3])

# Mostra quantas dimensões possui
print("\nDimensões de B:")
print(b.ndim)

# Mostra o formato
print("\nShape de B:")
print(b.shape)

# Mostra o array
print("\nArray B:")
print(b)


# ============================================================
# 9. ADICIONANDO UMA DIMENSÃO COM NEWAXIS
# ============================================================

# Adiciona uma nova dimensão
# Transforma o array em uma matriz com 1 linha e 3 colunas
b2 = b[np.newaxis, :]

print("\nB2:")
print(b2)

print("Dimensões:")
print(b2.ndim)

print("Shape:")
print(b2.shape)


# ============================================================
# 10. TRANSFORMANDO EM UMA COLUNA
# ============================================================

# Transforma o array em uma matriz vertical
# com 3 linhas e 1 coluna
b22 = b[:, np.newaxis]

print("\nB22:")
print(b22)

print("Dimensões:")
print(b22.ndim)

print("Shape:")
print(b22.shape)

# Acessa o terceiro elemento da primeira coluna
print("\nElemento da posição [2][0]:")
print(b22[2][0])


# ============================================================
# 11. CONCATENANDO ARRAYS
# ============================================================

# Cria dois arrays
c = np.array([1, 2, 3])
d = np.array([4, 5, 6])

# Junta C e D
e = np.concatenate((c, d))

# Junta D e C
f = np.concatenate((d, c))

print("\nConcatenação C + D:")
print(e)

print("\nConcatenação D + C:")
print(f)


# ============================================================
# 12. FILTROS BOOLEANOS
# ============================================================

# Cria uma matriz
g = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("\nArray G:")
print(g)

print("-----------------")

# Pega somente os números maiores que 8
maior_8 = g[g > 8]

print("\nNúmeros maiores que 8:")
print(maior_8)


# ============================================================
# 13. OPERAÇÕES ESTATÍSTICAS
# ============================================================

# Cria um array
h = np.array([1, 2, 3])

# Soma todos os valores
print("\nSoma:")
print(h.sum())

# Mostra o maior valor
print("\nMaior valor:")
print(h.max())

# Calcula a média
print("\nMédia:")
print(h.mean())

# Mostra o menor valor
print("\nMenor valor:")
print(h.min())

# Calcula o desvio padrão
print("\nDesvio padrão:")
print(h.std())

# Calcula a variância
print("\nVariância:")
print(h.var())


# ============================================================
# 14. NÚMEROS ALEATÓRIOS
# ============================================================

# Cria um gerador de números aleatórios
rng = default_rng()

# Cria números inteiros aleatórios de 0 até antes de 10
# em uma matriz de 2 linhas e 4 colunas
aleatorio = rng.integers(10, size=(2, 4))

print("\nArray aleatório:")
print(aleatorio)


# ============================================================
# 15. ARRAYS COM TIPOS DIFERENTES
# ============================================================

# Quando colocamos números e texto no mesmo array,
# o NumPy transforma os valores para um tipo compatível
o = np.array([1, "Daniel", 2, 3, 4, 5, 6, 7, 8])

print("\nArray com texto e números:")
print(o)

print("\nTipo da variável:")
print(type(o))

print("-----------------")


# ============================================================
# 16. LISTAS DO PYTHON
# ============================================================

# Cria uma lista comum do Python
lista_o = ["1", "Daniel", "2", "4", "5", "6", "7", "8"]

print("\nLista do Python:")
print(lista_o)


# ============================================================
# 17. SLICING - PEGANDO PARTES DE ARRAYS
# ============================================================

# Cria um array para praticar slicing
numeros = np.array([10, 20, 30, 40, 50, 60, 70])

print("\nArray original:")
print(numeros)

# Pega do índice 1 até antes do índice 5
print("\nDo índice 1 até antes do 5:")
print(numeros[1:5])

# Pega os primeiros 3 elementos
print("\nPrimeiros 3 elementos:")
print(numeros[:3])

# Pega do índice 3 até o final
print("\nDo índice 3 até o final:")
print(numeros[3:])

# Pega elementos pulando de 2 em 2
print("\nPulando de 2 em 2:")
print(numeros[::2])


# ============================================================
# 18. SLICING EM MATRIZES
# ============================================================

matriz = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("\nMatriz:")
print(matriz)

# Pega todas as linhas e as duas primeiras colunas
print("\nTodas as linhas e duas primeiras colunas:")
print(matriz[:, :2])

# Pega as duas primeiras linhas
print("\nDuas primeiras linhas:")
print(matriz[:2, :])

# Pega uma parte específica da matriz
print("\nParte da matriz:")
print(matriz[1:3, 1:3])


# ============================================================
# 19. RESHAPE - MUDANDO O FORMATO DO ARRAY
# ============================================================

# Cria um array com 12 números
array_reshape = np.arange(12)

print("\nArray original:")
print(array_reshape)

# Transforma o array em uma matriz de 3 linhas e 4 colunas
array_3x4 = array_reshape.reshape(3, 4)

print("\nArray transformado em 3x4:")
print(array_3x4)

# Transforma o mesmo array em 2 linhas e 6 colunas
array_2x6 = array_reshape.reshape(2, 6)

print("\nArray transformado em 2x6:")
print(array_2x6)


# ============================================================
# 20. BROADCASTING
# ============================================================

# Cria um array
broadcast = np.array([1, 2, 3])

print("\nArray original:")
print(broadcast)

# O NumPy adiciona 10 a todos os elementos
print("\nArray + 10:")
print(broadcast + 10)

# Multiplica todos os elementos por 2
print("\nArray * 2:")
print(broadcast * 2)


# Exemplo de broadcasting com matriz

matriz_broadcast = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Array que será aplicado em cada linha da matriz
valores = np.array([10, 20, 30])

print("\nMatriz:")
print(matriz_broadcast)

print("\nValores:")
print(valores)

# O NumPy soma os valores em cada linha
print("\nResultado do broadcasting:")
print(matriz_broadcast + valores)


# ============================================================
# 21. NP.WHERE - CONDIÇÕES
# ============================================================

# Cria um array de idades
idades = np.array([15, 18, 20, 16, 25])

print("\nIdades:")
print(idades)

# Se a idade for maior ou igual a 18,
# coloca "Maior de idade".
# Caso contrário, coloca "Menor de idade".
resultado = np.where(
    idades >= 18,
    "Maior de idade",
    "Menor de idade"
)

print("\nResultado usando np.where:")
print(resultado)


# ============================================================
# 22. NP.WHERE COM NÚMEROS
# ============================================================

notas = np.array([5, 8, 4, 10, 6])

# Se a nota for maior ou igual a 6,
# mantém a nota.
# Caso contrário, coloca 0.
notas_aprovadas = np.where(
    notas >= 6,
    notas,
    0
)

print("\nNotas originais:")
print(notas)

print("\nNotas aprovadas:")
print(notas_aprovadas)


# ============================================================
# FIM DO CÓDIGO
# ============================================================

print("\n==============================")
print("FIM DOS EXEMPLOS DE NUMPY!")
print("==============================")

