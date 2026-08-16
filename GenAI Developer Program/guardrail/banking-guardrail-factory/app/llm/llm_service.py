from typing import List


class LLMService:
    def __init__(self) -> None:
        pass

    def generate(self, prompt: str, context: List[str]) -> str:
        contextualized_prompt = f"Prompt: {prompt}\nContext: {context}"
        return f"Simulated LLM response for query: {prompt}\nUsing context from {len(context)} document(s)."
