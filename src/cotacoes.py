from typing import Dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from src.lista_moedas import lista_moedas
import io
import json
import os
from datetime import datetime


class Cotacoes():
    def executar(self) -> Dict[str, str]:
        """
        Função responsavel por inicializar os métodos da classe, retorna um
        dicionario contendo os dados obtidos.
        """
        self.__initializate()
        cotacoes = self.__get_cotacao()
        self.__save_json(cotacoes)
        self.__close()
        return cotacoes

    def __initializate(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.__navegador = webdriver.Chrome(options=chrome_options)

    def __get_cotacao(self) -> Dict[str, str]:
        cotacoes = {}
        for moeda in lista_moedas:
            self.__navegador.get('http://google.com.br/')
            barra_de_pesquisa = self.__navegador.find_element(
                By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]\
                    /div[2]/div[2]/input')
            barra_de_pesquisa.send_keys(f'Cotação {moeda}')
            barra_de_pesquisa.send_keys(Keys.ENTER)
            result = self.__navegador.find_element(
                By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]\
                    /div[1]/div[2]/span[1]').get_attribute('data-value')
            cotacoes[moeda] = result
        return cotacoes

    def __save_json(self, cotacao_var: Dict[str, str]) -> None:
        with open(os.path.join('files', 'cotacoes.json'), 'w') as arq:
            cotacao_var['last_att'] = datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S")
            json.dump(cotacao_var, arq,)

    def __close(self) -> None:
        self.__navegador.quit()
