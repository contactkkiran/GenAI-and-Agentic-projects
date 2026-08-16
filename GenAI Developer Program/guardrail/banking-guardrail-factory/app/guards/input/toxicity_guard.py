from app.factory.registry import GuardRegistry
from app.models.guardrail_result import GuardrailResult


class ToxicityGuard:
    def __init__(self, registry: GuardRegistry) -> None:
        self.registry = registry

    def validate(self, text: str) -> GuardrailResult:
        disallowed = ["hate", "terrorism", "bomb"]
        if self.registry.is_enabled("input", "toxicity_guard") and any(
            token in text.lower() for token in disallowed
        ):
            return GuardrailResult(False, "Toxic language detected in input")
        return GuardrailResult(True, "")
