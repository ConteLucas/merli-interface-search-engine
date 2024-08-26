from flask import Blueprint, request, jsonify
from src.app.dtos.request.search_engine_dto import SearchEngineDTO
from src.app.service.keyword_service import KeywordService

keyword_controller = Blueprint('keyword_controller', __name__)

keyword_service = KeywordService()


@keyword_controller.route('/process_keyword', methods=['POST'])
def process_keyword():
    try:
        data = request.json

        print("Dados da requisição:", data)

        auth_token = data.get('auth_token')
        user_id = data.get('user_id')
        keyword = data.get('keyword')

        dto = SearchEngineDTO(auth_token=auth_token, user_id=user_id, keyword=keyword)

        result = keyword_service.process_keyword(dto)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
