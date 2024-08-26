from pandas import DataFrame
from typing import Dict, List
from src.domain.entity.request.keyword_entity import KeywordEntity
from src.domain.usecases.etl.extract_data import ExtractData
from src.domain.usecases.etl.tranformer_data import TransformerData
from src.domain.usecases.etl.load_data import LoadData
from src.infra.database.database_provider import DatabaseProvider
from src.infra.mapper.mapper_model_keyword import MapperModelKeyword
from src.domain.utils.config_files_util import ConfigFilesUtil
from src.app.dtos.response.result_search_dto import ResultSearchDTO
from src.app.dtos.response.results_dto import ResultsDto


class KeywordUseCase:
    def __init__(self):
        self.config_util = ConfigFilesUtil()
        self.data_provider = DatabaseProvider()
        self.extractor = ExtractData(self.config_util)
        self.transformer = TransformerData()
        self.loader = LoadData(self.config_util)

    def handle_keyword(self, entity: KeywordEntity) -> Dict[str, str]:
        keyword = MapperModelKeyword.entity_to_model(entity)

        df = self._extract(keyword)
        if df is None or not isinstance(df, DataFrame):
            raise ValueError("Extraction failed or did not return a DataFrame.")

        transformed_payload = self._transform(df)
        if transformed_payload is None:
            raise ValueError("Transformation failed or returned None.")

        # Transformar os dados em instâncias de ResultsDto
        try:
            results_dto = [ResultsDto(index=item['index'], title=item['title'], link=item['link']) for item in
                           transformed_payload]
        except KeyError as e:
            raise ValueError(f"Transformed payload is missing expected keys: {e}")

        result_search_dto = ResultSearchDTO(results=results_dto)
        json_payload = result_search_dto.to_dict()

        # Atualizar ou inserir a palavra-chave no banco de dados
        if self.data_provider.get_keyword(keyword):
            self.data_provider.update_keyword(keyword)
        else:
            self.data_provider.insert_keyword(keyword)

        return {'status': '200: success', 'payload': json_payload}

    def _extract(self, keyword: str) -> DataFrame:
        try:
            df = self.extractor.extract(keyword)  # Passando a palavra-chave como string
            if df is None:
                print(f"Warning: Extraction returned None for keyword: {keyword}")
            else:
                print(f"Extraction successful for keyword: {keyword}")
            return df
        except Exception as e:
            print(f"Error during extraction: {e}")
            return None

    def _transform(self, df: DataFrame) -> List[dict]:
        try:
            transformed = self.transformer.transform(df)
            if transformed is None:
                print("Warning: Transformation returned None.")
            elif not isinstance(transformed, list):
                print(f"Warning: Transformation returned an unexpected type: {type(transformed)}")
            elif any(not isinstance(item, dict) or 'index' not in item or 'title' not in item or 'link' not in item for
                     item in transformed):
                print("Warning: Transformation returned invalid items.")
            else:
                print("Transformation successful.")
            return transformed
        except Exception as e:
            print(f"Error during transformation: {e}")
            return None

    def _load(self, payload: List[dict]) -> List[dict]:
        try:
            if payload is None:
                print("Warning: Loading returned None.")
            else:
                print("Loading successful.")
            return payload
        except Exception as e:
            print(f"Error during loading: {e}")
            return None
