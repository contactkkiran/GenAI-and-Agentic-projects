from app.factory.registry import GuardRegistry

from app.guards.input.pii_guard import PIIGuard
from app.guards.input.injection_guard import InjectionGuard


class GuardrailFactory:

    def __init__(self, registry: GuardRegistry) -> None:
        self.registry = registry

    def create_input_guardrails(self):

        guards = []

        if self.registry.is_enabled("input", "pii"):
            guards.append(PIIGuard())

        if self.registry.is_enabled("input", "prompt_injection"):
            guards.append(InjectionGuard())

        return guards
