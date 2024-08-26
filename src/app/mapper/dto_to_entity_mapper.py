from src.app.dtos.request.search_engine_dto import SearchEngineDTO
from src.domain.entity.request.keyword_entity import KeywordEntity


class DtoToEntityMapper:
    @staticmethod
    def dto_to_entity(dto: SearchEngineDTO) -> KeywordEntity:
        return KeywordEntity(
            keyword=dto.keyword,
            user_id=dto.user_id,
            auth_token=dto.auth_token
        )
