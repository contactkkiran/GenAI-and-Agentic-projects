from app.factory.registry import GuardRegistry
from app.models.guardrail_result import GuardrailResult


class ParameterGuard:
    def __init__(self, registry: GuardRegistry) -> None:
        self.registry = registry

    def validate(self, parameters: dict) -> GuardrailResult:
        if self.registry.is_enabled("tool", "parameter_guard") and not parameters:
            return GuardrailResult(False, "Tool parameters are required")
        return GuardrailResult(True, "")
