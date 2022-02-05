from src.cotacoes import Cotacoes
import json

if __name__ == "__main__":
    cotas = Cotacoes()
    cotacoes = cotas.executar()
    with open('files/cotacoes.json', 'r') as arq:
        data = json.load(arq)
 