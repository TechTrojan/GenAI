# Cost, Latency & Response Quality Evaluation

## Overview

I wanted to understand how different LLMs behave when you look beyond just “it works” and start measuring what actually matters in real systems — tokens, latency, and response quality.


The goal was simple: run the same set of questions across all three and observe how they differ in performance and output.

---

## 🧪 Experiment 2 — Prompt Caching with `claude-sonnet-4-5`

### What is Prompt Caching?

Prompt caching is a feature offered by Anthropic that allows a large, stable portion of the prompt (such as a system prompt) to be stored server-side between requests. Subsequent requests that share the same prefix read from that cache instead of reprocessing the full input, reducing the cost of input tokens significantly.

**How it works:**
- On the **first request**, the stable prefix is written to the cache (`cache_creation_input_tokens > 0`)
- On **subsequent requests**, that prefix is served from cache (`cache_read_input_tokens > 0`)
- Cache TTL is **5 minutes** by default (configurable up to 1 hour)
- Cache reads cost approximately **10% of the normal input token price**
- Cache writes cost approximately **125% of the normal input token price**

---

### Why `claude-sonnet-4-5`?

Each Claude model has a minimum token threshold before a prefix is eligible for caching:

| Model | Minimum tokens to cache |
|---|---|
| Opus 4.7, Opus 4.6, Haiku 4.5 | 4096 tokens |
| Sonnet 4.6, Haiku 3.5 | 2048 tokens |
| **Sonnet 4.5** | **1024 tokens** ✅ |

`claude-sonnet-4-5` has the lowest threshold, making it ideal for experimenting with a moderately sized system prompt without needing to pad content artificially.

---

### Experiment Setup

| Parameter | Value |
|---|---|
| Model | `claude-sonnet-4-5` |
| Total questions | 20 |
| System prompt size | **1236 tokens** (cached) |
| Cache TTL | 5 minutes (default) |
| Max output tokens | 3000 |
| Cache marker | `cache_control: {“type”: “ephemeral”}` on system prompt |

A detailed domain-expert system prompt (~1236 tokens) covering e-commerce, consumer electronics, cloud computing, and purchasing frameworks was placed at the start of every request and annotated with `cache_control`. The 20 questions varied freely — only the system prompt prefix was cached.

---

### Results

| Sr.No | Prompt Tokens | Response Tokens | Response Time (s) | Cache Created | Cache Read |
|---|---|---|---|---|---|
| 1 | 54 | 1645 | 36.3 | **1236** | 0 |
| 2 | 54 | 1356 | 31.7 | 0 | **1236** |
| 3 | 44 | 1891 | 44.3 | 0 | **1236** |
| 4 | 44 | 3000 | 63.2 | 0 | **1236** |
| 5 | 59 | 1805 | 46.8 | 0 | **1236** |
| 6 | 41 | 2249 | 55.4 | 0 | **1236** |
| 7 | 44 | 2294 | 59.2 | 0 | **1236** |
| 8 | 59 | 2701 | 64.8 | 0 | **1236** |
| 9 | 51 | 1639 | 41.4 | 0 | **1236** |
| 10 | 43 | 2741 | 68.7 | 0 | **1236** |
| 11 | 54 | 1448 | 35.7 | 0 | **1236** |
| 12 | 52 | 2191 | 51.2 | 0 | **1236** |
| 13 | 48 | 2349 | 62.1 | 0 | **1236** |
| 14 | 48 | 1303 | 32.8 | 0 | **1236** |
| 15 | 40 | 2216 | 58.4 | 0 | **1236** |
| 16 | 51 | 2430 | 61.5 | 0 | **1236** |
| 17 | 55 | 2200 | 50.0 | 0 | **1236** |
| 18 | 50 | 2179 | 46.8 | 0 | **1236** |
| 19 | 51 | 2768 | 60.6 | 0 | **1236** |
| 20 | 54 | 1984 | 51.9 | 0 | **1236** |

---

### Key Findings

#### ✅ Caching worked as expected
- Request 1 wrote **1236 tokens** to cache (`cache_creation_input_tokens = 1236`)
- Requests 2–20 all read **1236 tokens** from cache (`cache_read_input_tokens = 1236`)
- **19 out of 20 requests** received a cache hit — 95% hit rate

#### 💰 Cost Impact

Pricing for `claude-sonnet-4-5`: Input $3.00/1M tokens · Cache write $3.75/1M · Cache read $0.30/1M · Output $15.00/1M

| Cost Component | 20 Requests | 10,000 Requests |
|---|---|---|
| **Without caching** | | |
| Input tokens (full price) | $0.0771 | $38.57 |
| Output tokens | $0.6358 | $317.91 |
| **Total (no cache)** | **$0.7130** | **$356.48** |
| | | |
| **With caching** | | |
| Cache write (1 request) | $0.0046 | $0.0046 |
| Uncached input tokens (questions only) | $0.0030 | $1.49 |
| Cache read (19 / 9,999 requests) | $0.0070 | $3.71 |
| Output tokens | $0.6358 | $317.91 |
| **Total (with cache)** | **$0.6505** | **$323.12** |
| | | |
| **Input cost saving** | **81%** | **86.5%** |
| **Total cost saving** | **8.8%** | **9.4%** |

> Input savings are substantial (~81–87%), but output tokens dominate total spend. At scale, both effects compound — more requests amplify the cache read savings while the single write cost remains fixed.

#### ⏱️ Response Time — No Improvement (Expected)
Response time showed **no consistent reduction** after the first request. This is by design:

> **Prompt caching reduces cost, not latency.**

Response time is dominated by **output token generation**, not input processing. The strong correlation between `response_tokens` and `total_response_time` confirms this:

| Response Tokens | Response Time (s) |
|---|---|
| 1303 (min) | 32.8 (fastest) |
| 3000 (max) | 63.2 (slowest) |
| ~2100 (avg) | ~51 (avg) |

The ~18ms saved by skipping input reprocessing is negligible compared to the seconds required to stream 1300–3000 output tokens.

---

### What Prompt Caching Does and Does Not Do

| | Prompt Caching |
|---|---|
| Reduces input token **cost** | ✅ Yes — ~90% cheaper per cache read |
| Reduces **response time** | ❌ No — output generation dominates latency |
| Requires opt-in | ✅ Yes — add `cache_control` to the content block |
| Works automatically after first request | ✅ Yes — within the TTL window |
| Minimum prefix size | ✅ 1024 tokens for `claude-sonnet-4-5` |

---

### Implementation

**Python (Anthropic SDK):**
```python
response = client.messages.create(
    model=”claude-sonnet-4-5”,
    max_tokens=3000,
    system=[
        {
            “type”: “text”,
            “text”: SYSTEM_PROMPT,
            “cache_control”: {“type”: “ephemeral”},  # marks this block for caching
        }
    ],
    messages=[{“role”: “user”, “content”: question}],
)

# Read cache usage from response
cache_created = response.usage.cache_creation_input_tokens  # > 0 on first request
cache_read    = response.usage.cache_read_input_tokens      # > 0 on subsequent requests
```

---

## What I Built

A lightweight evaluation pipeline using:

- Anthropic SDK for API calls  
- Python script to run tests and collect metrics  

The model receives a set of 20 questions and I capture:

- Token usage (prompt, response, cached)  
- Latency  

---

## Evaluation Flow

1. Define a fixed set of 20 questions  
2. Send each question to the model with a cached system prompt  
3. Capture:
   - Tokens used (prompt, response, cache created, cache read)  
   - Response time  
4. Store results in CSV  

---

## Metrics Considered

### 1. Token Usage
Tracks how many tokens the model consumes per request, broken down into:
- **Prompt tokens** — uncached input tokens (the question)
- **Response tokens** — output tokens generated
- **Cache creation tokens** — system prompt tokens written to cache (first request only)
- **Cache read tokens** — system prompt tokens served from cache (subsequent requests)

Why it matters:
- Direct impact on cost  
- Cache read tokens cost ~10% of normal input token price  

---

### 2. Latency
Measures end-to-end response time per request.

Why it matters:
- Dominated by output token generation, not input processing  
- Prompt caching does not reduce latency  

---

## 📊 Evaluation Results

### 🔹 Anthropic – `claude-sonnet-4-5`

- **Token Usage:**  
  Response tokens ranged from **1303 to 3000**, reflecting the varying complexity of the 20 questions. Prompt tokens per question were small (40–59 tokens), as only the question itself was uncached.

- **Prompt Caching:**  
  The system prompt (1236 tokens) was written to cache on request 1 and read from cache on all 19 subsequent requests, achieving a **95% cache hit rate**.

- **Latency:**  
  Response times ranged from **31.7 to 68.7 seconds**, driven entirely by output token count — not input processing. No latency improvement was observed from caching.

---

## 🧠 Summary Insights

- **Prompt caching reduces input cost** — cached tokens cost ~10% of the normal price, yielding ~84% savings on the system prompt across 20 requests.  
- **Prompt caching does not reduce latency** — response time scales with output tokens, not input tokens.  
- **Cache hit rate was 95%** — 19 out of 20 requests read the system prompt from cache within the 5-minute TTL window.  

---

## Why This Experiment Matters

Prompt caching is a cost optimisation tool, not a latency optimisation tool.

Understanding this distinction helps in:
- Designing systems with large stable system prompts (RAG context, instructions, few-shot examples)  
- Accurately estimating cost savings before deploying at scale  
- Avoiding the false assumption that caching will speed up responses  

---

## Possible Extensions

- Test with a 1-hour TTL to observe cache persistence across separate runs  
- Measure cost savings at higher request volumes (100+ requests)  
- Compare caching behaviour across Sonnet 4.5, Sonnet 4.6, and Opus models  
- Visualize token breakdown and cost per request  

---

## How to Run

1. Clone the repo  
2. Add `ANTHROPIC_API_KEY` to a `.env` file  
3. Install dependencies: `pip install anthropic python-dotenv`  
4. Run: `python Experiment.py`  
5. Review `Anthropic_result.csv` for results  

---

## Repo

https://github.com/TechTrojan/GenAI/tree/Prompt_Caching

---

## Final Thought

Prompt caching is one of those features that pays for itself quietly.

The savings are real, the implementation is minimal, and understanding where the cost actually comes from — output tokens, not input — changes how you design LLM-powered systems.

---

## References

### This Experiment
- [Experiment source code — Prompt_Caching branch](https://github.com/TechTrojan/GenAI/tree/Prompt_Caching)
- [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)

### Prompt Caching — Official Documentation

| Provider | Model(s) | Documentation |
|---|---|---|
| **Anthropic** | Claude Sonnet, Opus, Haiku | [Prompt Caching Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) |
| **OpenAI** | GPT-4o, GPT-4o mini, o-series | [Prompt Caching Guide](https://platform.openai.com/docs/guides/prompt-caching) |
| **Google Gemini** | Gemini 1.5 Pro, Flash | [Context Caching Guide](https://ai.google.dev/gemini-api/docs/caching) |
| **Google Vertex AI** | Gemini on Vertex | [Context Caching (Vertex)](https://cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview) |
| **Amazon Bedrock** | Claude via Bedrock | [Prompt Caching on Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) |

### Prompt Caching Pricing

| Provider | Cache Write | Cache Read | Pricing Reference |
|---|---|---|---|
| **Anthropic** | 125% of input price | 10% of input price | [Prompt Caching Pricing](https://www.anthropic.com/pricing#prompt-caching) |
| **OpenAI** | No explicit write charge (automatic) | 50% of input price | [Prompt Caching Pricing](https://platform.openai.com/docs/guides/prompt-caching#what-is-cached) |
| **Google Gemini API** | Storage charged per token per hour | 25% of input price | [Context Caching Pricing](https://ai.google.dev/gemini-api/docs/caching?lang=python#pricing) |
| **Google Vertex AI** | Storage charged per token per hour | 25% of input price | [Context Caching Pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing#context-caching) |
| **Amazon Bedrock** | 125% of input price | 10% of input price | [Prompt Caching Pricing](https://aws.amazon.com/bedrock/pricing/#Prompt_Caching) |
