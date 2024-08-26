import json
from pandas import DataFrame


class LoadData:
    def __init__(self, config_files_util):
        self.config_files_util = config_files_util
        self.output_file = self.config_files_util.get('OUTPUT_FILE')  # Nome do arquivo de saída

    def load(self, df: DataFrame) -> None:
        if df.empty:
            print("Nenhum dado para processar.")
            return

        payload = []
        for _, row in df.iterrows():
            record = {
                "index": row['Index'],
                "title": row['Title'],
                "link": row['Link']
            }
            payload.append(record)

        with open(self.output_file, 'w') as file:
            json.dump(payload, file, indent=4)

        print(f"Dados salvos em {self.output_file}.")
