from app.factory.registry import GuardRegistry
from app.factory.guardrail_factory import GuardrailFactory


class InputGuardrailPipeline:

    def __init__(self, registry: GuardRegistry) -> None:
        self.factory = GuardrailFactory(registry)
        self.guardrails = self.factory.create_input_guardrails()

    def validate(self, text: str):

        for guardrail in self.guardrails:

            result = guardrail.check(text)

            print(f"[{result.guardrail}] " f"{'PASS' if result.allowed else 'BLOCK'}")

            if not result.allowed:
                return result

        return {"allowed": True, "message": "Input passed all guardrails."}
