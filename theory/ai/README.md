# AI / LLM Systems

`Weeks 27–35` of the prep plan. AI system design rounds are now common at product companies.

| # | File | Topics |
|---|---|---|
| 01 | [LLM Systems Overview](01-llm-systems.md) | the framing, prompt vs RAG vs fine-tune, agents, serving, evals, safety |
| 02 | [RAG](02-rag.md) | chunking, vector search, hybrid + reranking, query rewriting, RAG evaluation |
| 03 | [Agents & Serving](03-agents-and-serving.md) | the agent loop, workflow vs agent, multi-agent, caching, latency, model routing |
| 04 | [Evals, Observability & Safety](04-evals-and-safety.md) | golden sets, LLM-as-judge, drift, hallucination, prompt injection, PII |

## The eight sentences worth memorising

1. *"An LLM is a **reasoning engine, not a knowledge store**."*
2. *"**Debug retrieval before the model** — measure recall@k separately."*
3. *"Fine-tuning teaches **how to behave**; RAG teaches **what it knows**."*
4. *"**Most of what people call agents should be workflows**."*
5. *"**The first thing I'd build is the eval set**."*
6. *"**Validate the judge** against human labels."*
7. *"Prompt injection can't be prevented at the prompt layer — you **contain the blast radius**."*
8. *"For high-volume narrow prediction, a **trained model beats an LLM** on every axis."*

## Connections

| AI concept | Where it reappears |
|---|---|
| Vector ANN indexes | [DSA: graphs](../../patterns/graphs/) — HNSW is a proximity graph |
| Semantic / prompt caching | [System Design: caching](../system-design/05-replication-sharding-caching.md) |
| Queues for async inference | [System Design: messaging](../system-design/06-messaging-and-kafka.md) |
| GC pauses → p99 | [OS: memory](../os/04-memory-management.md) |
| PII in traces and embeddings | [System Design: security](../system-design/09-apis-and-security.md) |
