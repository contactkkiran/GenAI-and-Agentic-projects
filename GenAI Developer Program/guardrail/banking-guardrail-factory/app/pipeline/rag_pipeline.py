from typing import List

from app.factory.registry import GuardRegistry
from app.llm.llm_service import LLMService
from app.models.guardrail_result import GuardrailResult
from app.rag.retriever import Retriever


class RAGPipeline:
    def __init__(
        self, retriever: Retriever, llm: LLMService, registry: GuardRegistry
    ) -> None:
        self.retriever = retriever
        self.llm = llm
        self.registry = registry

    def run(self, query: str) -> str:
        context = self.retriever.retrieve(query)
        response = self.llm.generate(query, context)
        return response
