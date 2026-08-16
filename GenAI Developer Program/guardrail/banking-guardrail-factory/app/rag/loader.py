from pathlib import Path
from typing import List


class Loader:
    def __init__(self, knowledge_dir: Path) -> None:
        self.knowledge_dir = knowledge_dir

    def load_documents(self) -> List[str]:
        documents = []
        for path in sorted(self.knowledge_dir.glob("*.pdf")):
            documents.append(str(path))
        return documents
