import re

from app.guards.base_guard import BaseGuardrail
from app.models.guardrail_result import GuardrailResult


class PIIGuard(BaseGuardrail):

    @property
    def name(self) -> str:
        return "PII"

    def check(self, text: str) -> GuardrailResult:

        account_pattern = r"\b\d{10,16}\b"

        if re.search(account_pattern, text):
            return GuardrailResult(
                allowed=False,
                guardrail=self.name,
                reason="Possible bank account number detected.",
            )

        return GuardrailResult(allowed=True, guardrail=self.name)
