User
 ↓
PII Guard       → PASS
 ↓
Injection Guard → BLOCK ❌
 ↓
LLM             → NEVER CALLED
Important note : That's actually an important benefit: you stop unsafe requests before spending tokens/latency on RAG and the LLM.

One subtle point: not every guardrail belongs before the LLM. For example, hallucination_guard and grounding_guard need the generated response, so they belong after the LLM.

So your Factory will eventually have methods like:
create_input_guardrails()
create_retrieval_guardrails()
create_tool_guardrails()
create_output_guardrails()

Each method creates the appropriate guards for that stage. That's the architecture we're going to build.
