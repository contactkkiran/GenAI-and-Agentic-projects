from app.factory.registry import GuardRegistry
from app.models.guardrail_result import GuardrailResult


class DataFilterGuard:
    def __init__(self, registry: GuardRegistry) -> None:
        self.registry = registry

    def validate(self, data: str) -> GuardrailResult:
        if (
            self.registry.is_enabled("retrieval", "data_filter_guard")
            and "restricted" in data.lower()
        ):
            return GuardrailResult(
                False, "Restricted data present in retrieval results"
            )
        return GuardrailResult(True, "")
