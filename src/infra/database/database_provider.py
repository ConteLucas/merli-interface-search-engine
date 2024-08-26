from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from src.domain.utils.config_files_util import ConfigFilesUtil
from src.infra.database.models.keywords_model import KeywordsModel


class DatabaseProvider:
    def __init__(self):
        self.config_util = ConfigFilesUtil()
        self.database_url = 'postgresql://postgres:1234@localhost:5433/postgres'
        print(self.database_url)

        self.engine = create_engine(self.database_url)
        self.Session = sessionmaker(bind=self.engine)

    def get_keyword(self, keyword_model: KeywordsModel) -> bool:
        session = self.Session()
        try:
            keyword = keyword_model.keyword
            result = session.execute(
                text("SELECT COUNT(*) FROM merli.keywords WHERE keyword = :keyword"),
                {"keyword": keyword}
            ).scalar()
            return result > 0
        finally:
            session.close()

    def update_keyword(self, keyword_model: KeywordsModel):
        session = self.Session()
        try:
            keyword = keyword_model.keyword
            session.execute(
                text(
                    "UPDATE merli.keywords SET search_count = search_count + 1, updated_date = CURRENT_TIMESTAMP "
                    "WHERE keyword = :keyword"
                ),
                {"keyword": keyword}
            )
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def insert_keyword(self, keyword_model: KeywordsModel):
        session = self.Session()
        try:
            keyword = keyword_model.keyword
            user_id = keyword_model.user_id
            auth_token = keyword_model.auth_token
            session.execute(
                text(
                    "INSERT INTO merli.keywords (keyword, search_count, user_id, auth_token, created_date) "
                    "VALUES (:keyword, 1, :user_id, :auth_token, CURRENT_TIMESTAMP)"
                ),
                {"keyword": keyword, "user_id": user_id, "auth_token": auth_token}
            )
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


