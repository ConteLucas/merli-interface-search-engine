class ResultsDto:
    def __init__(self, index: int, title: str, link: str):
        self.index = index
        self.title = title
        self.link = link

    def to_dict(self):
        return {
            "index": self.index,
            "title": self.title,
            "link": self.link
        }
