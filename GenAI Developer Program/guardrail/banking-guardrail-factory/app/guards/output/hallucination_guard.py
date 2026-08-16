from app.factory.registry import GuardRegistry
from app.models.guardrail_result import GuardrailResult


class HallucinationGuard:
    def __init__(self, registry: GuardRegistry) -> None:
        self.registry = registry

    def validate(self, text: str) -> GuardrailResult:
        if (
            self.registry.is_enabled("output", "hallucination_guard")
            and "not sure" in text.lower()
        ):
            return GuardrailResult(False, "Potential hallucination detected in output")
        return GuardrailResult(True, "")
