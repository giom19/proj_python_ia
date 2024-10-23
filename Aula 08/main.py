import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Ler arquivo csv pelo pandas 
def ler_csv(file_path):
    return pd.read_csv(file_path)
# Selecionando as colunas de entrada
def treinar(df):
    x = df[['acidez','densidade','viscosidade','tonalidade']]
    y = df['tipo_de_vinho']

#Dividindo os dados em dois tipos de treino
    x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2,random_state=42)

# Usando Random como exemplo 
    model = RandomForestClassifier()
    model.fit(x_train,y_train)
    # Avaliar modelo e precisão 
    y_pred = model.predict(x_test)
    precisao = accuracy_score(y_test,y_pred)
    print(f"Precisao: {precisao * 100:2f}%")

    return model

# Prever o vinho
def prever_vinho(model,acidez,densidade,viscosidade,tonalidade):
    # Criar um Dataframe com o mesma estrutura usada no treinamento
    entrada = pd.DataFrame({
        'acidez' : [acidez],
        'densidade' : [densidade],
        'viscosidade' : [viscosidade],
        'tonalidade' : [tonalidade]
    })
    entrada = [[acidez,densidade,viscosidade,tonalidade]]
    predicao = model.predict(entrada)
    probabilidade = model.predict_proba(entrada)

    return predicao[0],max(probabilidade[0])*100

# Metodo principal
if __name__ == "__main__":
    #Variavel que armazena nome do arquivo csv
    arquivo = 'vinho.csv'
    df = ler_csv(arquivo)
    model = treinar(df)

    #Entrada de dados pelo usuario
    acidez = 1
    densidade = 0.5
    viscosidade = 0.8
    tonalidade = 0.7

    vinho = prever_vinho(model,acidez,densidade,viscosidade,tonalidade)
    certeza = prever_vinho(model,acidez,densidade,viscosidade,tonalidade)

    print(f"O tipo de vinho é : {vinho}")
    print(f"{certeza:.2f}% de confiança")