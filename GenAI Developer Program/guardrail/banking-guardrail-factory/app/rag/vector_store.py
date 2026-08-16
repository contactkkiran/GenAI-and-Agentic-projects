from typing import Any, List


class VectorStore:
    def __init__(self) -> None:
        self.documents: List[Any] = []

    def add_documents(self, docs: List[Any]) -> None:
        self.documents.extend(docs)

    def search(self, query: str, top_k: int = 5) -> List[Any]:
        return self.documents[:top_k]
