import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
from src.domain.utils.config_files_util import ConfigFilesUtil
from src.infra.database.models.keywords_model import KeywordsModel


class ExtractData:

    def __init__(self, config_files_util: ConfigFilesUtil):
        self.config_util = config_files_util
        self.html_config = self.config_util.get('HTML')

    def extract(self, keyword: KeywordsModel) -> DataFrame:

        response = requests.get(self.html_config.get('URL') + keyword.keyword)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            item_list = soup.find('ol', class_=self.html_config.get('ITEM_LIST'))

            if item_list:
                items = item_list.find_all('li', class_=self.html_config.get('ITEMS'))
                product_array = []

                for index, item in enumerate(items):
                    link_tag = item.find('a', class_=self.html_config.get('LINK_TAG'))
                    title_tag = item.find('h2', class_=self.html_config.get('TITLE_TAG'))

                    if title_tag and link_tag:
                        title = title_tag.get_text()
                        link = link_tag['href']
                        product_array.append((index, title, link))

                df = pd.DataFrame(product_array, columns=['Index', 'Title', 'Link'])
                return df
            else:
                print("Nenhuma lista encontrada com a classe especificada.")
                return pd.DataFrame()
        else:
            print(f"Falha ao acessar a página. Status code: {response.status_code}")
            return pd.DataFrame()
