from app.factory.registry import GuardRegistry
from app.pipeline.input_pipeline import InputGuardrailPipeline

registry = GuardRegistry()

registry.register_config(
    {
        "guards": {
            "input": {"pii": {"enabled": True}, "prompt_injection": {"enabled": True}}
        }
    }
)

pipeline = InputGuardrailPipeline(registry)

result = pipeline.validate("What is my account balance?")

print("\nResult:")
print(result)
