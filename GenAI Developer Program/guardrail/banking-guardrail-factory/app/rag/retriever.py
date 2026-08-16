from typing import List


class Retriever:
    def __init__(self, loader) -> None:
        self.loader = loader

    def retrieve(self, query: str) -> List[str]:
        return self.loader.load_documents()
