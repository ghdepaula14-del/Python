from sklearn.linear_model import LinearRegression

# Dados de entrada
X = [[1], [2], [3], [4], [5]]

# Respostas
y = [3, 5, 7, 9, 11]

# Cria o modelo
modelo = LinearRegression()

# Treina o modelo
modelo.fit(X, y)

# Mostra o que o modelo aprendeu
print("Coeficiente:", modelo.coef_)
print("Intercepto:", modelo.intercept_)

# Faz uma previsão
previsao = modelo.predict([[6]])

print("Previsão para X = 6:", previsao)