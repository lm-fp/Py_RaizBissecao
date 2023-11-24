# Função cúbica
def funcao_cubica(x, coeficientes):
    a, b, c, d = coeficientes
    return a * x**3 + b * x**2 + c * x + d

# Método da Bisseção para encontrar raiz
def metodo_bissecao(coeficientes, a_intervalo, b_intervalo, tolerancia=0.0001):
    a, b, c, d = coeficientes
    fa = funcao_cubica(a_intervalo, coeficientes)
    fb = funcao_cubica(b_intervalo, coeficientes)

    if fa * fb >= 0:
        return None  # Não há raiz no intervalo fornecido

    while (b_intervalo - a_intervalo) >= tolerancia:
        ponto_medio = (a_intervalo + b_intervalo) / 2
        fm = funcao_cubica(ponto_medio, coeficientes)

        if fm == 0:
            return ponto_medio
        else:
            if fa * fm < 0:
                b_intervalo = ponto_medio
            else:
                a_intervalo = ponto_medio

    return (a_intervalo + b_intervalo) / 2


# Solicitar os coeficientes da equação cúbica
print("Insira os coeficientes da equação cúbica ax^3 + bx^2 + cx + d = 0")
a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))
d = float(input("Coeficiente d: "))

# Criar a lista de coeficientes
coeficientes = [a, b, c, d]

# Intervalo inicial
a_intervalo = float(input("Digite o limite inferior do intervalo: "))
b_intervalo = float(input("Digite o limite superior do intervalo: "))

# Encontrando a raiz da equação cúbica usando o método da Bisseção
raiz_bissecao = metodo_bissecao(coeficientes, a_intervalo, b_intervalo)

if raiz_bissecao is not None:
    print(f"A raiz da equação (método da Bisseção) é aproximadamente: {raiz_bissecao}")
else:
  print("Não foi possível encontrar uma raiz no intervalo fornecido.")