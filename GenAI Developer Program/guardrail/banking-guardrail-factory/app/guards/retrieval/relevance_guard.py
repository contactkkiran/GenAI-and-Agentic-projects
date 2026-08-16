from app.factory.registry import GuardRegistry
from app.models.guardrail_result import GuardrailResult


class RelevanceGuard:
    def __init__(self, registry: GuardRegistry) -> None:
        self.registry = registry

    def validate(self, context: str) -> GuardrailResult:
        if self.registry.is_enabled("retrieval", "relevance_guard") and not context:
            return GuardrailResult(False, "No relevant retrieval context available")
        return GuardrailResult(True, "")
