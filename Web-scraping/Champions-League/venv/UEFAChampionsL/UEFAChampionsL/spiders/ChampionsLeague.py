import scrapy
import pandas as pd
from itertools import zip_longest

class ChampionsleagueSpider(scrapy.Spider):
    name = "ChampionsLeague"
    allowed_domains = ["es.wikipedia.org"]
    start_urls = ["https://es.wikipedia.org/wiki/Anexo:Finalistas_de_la_Liga_de_Campeones_de_la_UEFA"]

    def parse(self, response):
        fechas = []
        campeon = []
        subcapeon =[]

        #establecemos la tabla
        for table in response.xpath('//table'):
            if len(table.xpath('tbody//tr')) == 72:
                table = table
                break
        #ya seleccionada la tabla correcta ciclamos para sacar las fechas
        for row in table.xpath('tbody//tr//td'):
            try:
                fecha = row.xpath('text()')[0].get()
                fechas.append(fecha)
                print(fecha)

            except IndexError:
                pass
        #ciclo para los ganadores
        for row in table.xpath('tbody//tr//td/b//a'):
            try:
                campeones = row.xpath('text()')[0].get()
                campeon.append(campeones)
                print(campeones)
            except IndexError:
                pass
        #parasubcampeon
        for row in table.xpath('.//tr'):
            try:
                subcap = row.xpath('.//td[4]/a/text()')
                print(subcap[0])
                subcapeon.append(subcap[0])
            except IndexError:
                pass
        # Crear un DataFrame con los datos extraídos
        fechas = [fecha for fecha in fechas if fecha.strip()]
        campeon = [elemento for elemento in campeon if len(elemento) > 5]
        data = list(zip_longest(fechas, campeon, subcapeon))
        df = pd.DataFrame(data, columns=["Fecha", "Campeón","subcampeon"])

        # Guardar el DataFrame en un archivo CSV
        df.to_csv("champions_league_data.csv", index=False)

        # También puedes imprimir el DataFrame para verificarlo
        print(df)