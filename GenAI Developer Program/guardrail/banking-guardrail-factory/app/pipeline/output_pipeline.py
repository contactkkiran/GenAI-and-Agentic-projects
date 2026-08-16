from app.factory.registry import GuardRegistry
from app.guards.output.pii_guard import PiiGuard as OutputPiiGuard
from app.guards.output.hallucination_guard import HallucinationGuard
from app.guards.output.grounding_guard import GroundingGuard
from app.guards.output.policy_guard import PolicyGuard as OutputPolicyGuard


class OutputPipeline:
    def __init__(self, registry: GuardRegistry) -> None:
        self.registry = registry
        self.guards = [
            OutputPiiGuard(registry),
            HallucinationGuard(registry),
            GroundingGuard(registry),
            OutputPolicyGuard(registry),
        ]

    def validate(self, output: str) -> str:
        failures = [
            guard.validate(output)
            for guard in self.guards
            if not guard.validate(output).passed
        ]
        if failures:
            raise ValueError(
                "Output validation failed: " + "; ".join(f.details for f in failures)
            )
        return output
