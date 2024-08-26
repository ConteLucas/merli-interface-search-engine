from src.domain.entity.request.keyword_entity import KeywordEntity
from src.infra.database.models.keywords_model import KeywordsModel


class MapperModelKeyword:
    @staticmethod
    def entity_to_model(entity: KeywordEntity) -> KeywordsModel:
        return KeywordsModel(
            keyword=entity.keyword,
            user_id=entity.user_id,
            auth_token=entity.auth_token,
        )
