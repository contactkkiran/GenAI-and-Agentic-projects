from app.factory.registry import GuardRegistry
from app.models.guardrail_result import GuardrailResult


class GroundingGuard:
    def __init__(self, registry: GuardRegistry) -> None:
        self.registry = registry

    def validate(self, text: str) -> GuardrailResult:
        if (
            self.registry.is_enabled("output", "grounding_guard")
            and "according to" not in text.lower()
        ):
            return GuardrailResult(False, "Output lacks grounding references")
        return GuardrailResult(True, "")
