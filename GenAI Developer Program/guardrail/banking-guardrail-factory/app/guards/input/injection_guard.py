from app.guards.base_guard import BaseGuardrail
from app.models.guardrail_result import GuardrailResult


class InjectionGuard(BaseGuardrail):

    @property
    def name(self) -> str:
        return "PromptInjection"

    def check(self, text: str) -> GuardrailResult:

        patterns = [
            "ignore previous instructions",
            "ignore all instructions",
            "reveal system prompt",
            "bypass safety",
        ]

        normalized = text.lower()

        for pattern in patterns:
            if pattern in normalized:
                return GuardrailResult(
                    allowed=False,
                    guardrail=self.name,
                    reason=f"Potential prompt injection detected: {pattern}",
                )

        return GuardrailResult(allowed=True, guardrail=self.name)
