from app.factory.registry import GuardRegistry
from app.models.guardrail_result import GuardrailResult


class PolicyGuard:
    def __init__(self, registry: GuardRegistry) -> None:
        self.registry = registry

    def validate(self, text: str) -> GuardrailResult:
        if (
            self.registry.is_enabled("input", "policy_guard")
            and "fraud" in text.lower()
        ):
            return GuardrailResult(False, "Input violates internal banking policy")
        return GuardrailResult(True, "")
