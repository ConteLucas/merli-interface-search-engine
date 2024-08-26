from typing import List
from src.app.dtos.response.results_dto import ResultsDto


class ResultSearchDTO:
    def __init__(self, results: List[ResultsDto]):
        self.results = results

    def to_dict(self) -> dict:
        return {'results': [result.to_dict() for result in self.results]}
