from src.app.dtos.request.search_engine_dto import SearchEngineDTO
from src.app.mapper.dto_to_entity_mapper import DtoToEntityMapper
from src.domain.usecases.handler.keyword_usecase import KeywordUseCase


class KeywordService:
    def __init__(self):
        self.use_case = KeywordUseCase()

    def process_keyword(self, dto: SearchEngineDTO):
        entity = DtoToEntityMapper.dto_to_entity(dto)

        result = self.use_case.handle_keyword(entity)
        return result
