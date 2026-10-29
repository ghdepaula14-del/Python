from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dados
X = [[1], [2], [3], [4], [5], [6]]
y = [4, 5, 6, 7, 8, 9]

# Divide os dados
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Cria o modelo
modelo = LinearRegression()

# Treina
modelo.fit(X_treino, y_treino)

# Faz previsões usando os dados de teste
previsoes = modelo.predict(X_teste)

print("Dados de teste:")
print(X_teste)

print("\nRespostas verdadeiras:")
print(y_teste)

print("\nPrevisões do modelo:")
print(previsoes)


resultado = modelo.score(X_teste, y_teste)

print("\nScore:")
print(resultado)