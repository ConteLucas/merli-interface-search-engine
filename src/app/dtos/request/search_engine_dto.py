class SearchEngineDTO:
    def __init__(self, auth_token: str, user_id: str, keyword: str):
        self.auth_token = auth_token
        self.user_id = user_id
        self.keyword = keyword
