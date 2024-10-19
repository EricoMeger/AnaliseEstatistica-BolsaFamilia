class Calculator():
    def __init__(self):
        pass 

    def calc_media(self, items):
        return sum(items) / len(items) if len(items) > 0 else 0

    def calc_mediana(self, items):
        if len(items) % 2 == 0:
            return items[len(items+1) // 2]
        
        return items[((len(items) // 2) + ((len(items) // 2) + 1)) // 2]

    def calc_moda(self, items):
        frequencia = {}
        for item in items:
            if item not in frequencia:
                frequencia[item] = 1
            else:
                frequencia[item] += 1
        
        maior_freq = max(frequencia.values())

        moda = []
        for key, valor in frequencia.items():
            if valor == maior_freq:
                moda.append((key, valor))

        return moda

    def calc_varianca(self, items):
        media = self.calc_media(items)
        
        varianca = 0

        for item in items:
            varianca += (item - media) ** 2

        return varianca / (len(items) - 1) if len(items) > 1 else 0


    def calc_desvio_padrao(self, items):
        return self.calc_varianca(items) ** (1/2)

    def calcula_total_anual(self, items):
        total_anual = {}
        for _, row in items.iterrows():
            ano = row['year']
            familias = row['families']
            familias_baixa_renda = row['low_income_families']
            
            if ano not in total_anual:
                total_anual[ano] = {'total_familias': 0, 'total_familias_baixa_renda': 0}
                
            total_anual[ano]['total_familias'] += familias
            total_anual[ano]['total_familias_baixa_renda'] += familias_baixa_renda
            
        return total_anual

    def calc_pearson(self, x, y):
        n = len(x)
        somatorio_x = sum(x)
        somatorio_y = sum(y)
        somatorio_x_sqrd = sum([i ** 2 for i in x])
        somatorio_y_sqrd = sum([i ** 2 for i in y])

        somatorio_xy = 0
        for i, j in zip(x, y):
            somatorio_xy += i * j

        numerador = somatorio_xy - ((somatorio_x * somatorio_y) / n)
        denominador = ((somatorio_x_sqrd - (somatorio_x ** 2) / n) * (somatorio_y_sqrd - (somatorio_y ** 2) / n)) ** (1/2)

        pearson = numerador / denominador if denominador != 0 else None

        return pearson, self.get_correlation(pearson)

    def get_correlation(self, correlation):
        if correlation is None:
            return "Não há correlação"
        
        correlation = abs(correlation)

        if correlation == 0:
            return "Correlação nula"

        if correlation > 0 and correlation <= 0.3:
            return "Correlação fraca"
        
        if correlation > 0.3 and correlation <= 0.6:
            return "Correlação moderada"

        if correlation > 0.6 and correlation <= 0.9:
            return "Correlação forte"
        
        if correlation > 0.9 and correlation < 1:
            return "Correlação muito forte"

        return "Correlação perfeita"
    
    def calc_regression(self, x, y):
        n = len(x)
        media_x = self.calc_media(x)
        media_y = self.calc_media(y)

        numerador_beta = []
        for xi, yi in zip(x, y):
            numerador_beta.append((xi - media_x) * (yi - media_y))
        
        denominador_beta = []
        for xi in x:
            denominador_beta.append((xi - media_x) ** 2)

        beta = sum(numerador_beta) / sum(denominador_beta)

        alpha = media_y - (beta * media_x)

        return alpha, beta

    def predict_values(self, alpha, beta, items):
        predicted_values = []

        for x in items:
            predicted_values.append(alpha + (beta * x))

        return predicted_values