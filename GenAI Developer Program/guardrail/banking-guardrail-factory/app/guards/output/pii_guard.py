from app.factory.registry import GuardRegistry
from app.models.guardrail_result import GuardrailResult


class PiiGuard:
    def __init__(self, registry: GuardRegistry) -> None:
        self.registry = registry

    def validate(self, text: str) -> GuardrailResult:
        if self.registry.is_enabled("output", "pii_guard") and "ssn" in text.lower():
            return GuardrailResult(False, "PII detected in output")
        return GuardrailResult(True, "")
