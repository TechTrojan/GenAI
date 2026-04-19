# Cost, Latency & Response Quality Evaluation

## Overview

I wanted to understand how different LLMs behave when you look beyond just “it works” and start measuring what actually matters in real systems — tokens, latency, and response quality.

This small experiment compares three models:

- mistral-small-latest  
- gpt-4o-mini  
- claude-sonnet-4-6  

The goal was simple: run the same set of questions across all three and observe how they differ in performance and output.

---

## What I Built

A lightweight evaluation pipeline using:

- LangChain for orchestration  
- MistralAI + other model APIs for execution  
- Python script to run tests and collect metrics  

Each model receives the same set of 10 questions, and I capture:

- Token usage  
- Latency  
- Response output (for quality evaluation)  

---

## 🧠 Architecture Diagram

<p align="center">
  <img src="./assets/images/architecture.png" alt="Architecture Diagram" width="900"/>
</p>

---

## Evaluation Flow

1. Define a fixed set of 10 questions  
2. Send each question to all 3 models  
3. Capture:
   - Tokens used  
   - Response time  
   - Generated answer  
4. Store results  
5. Compare across models  

---

## Metrics Considered

### 1. Token Usage
Tracks how many tokens each model consumes per request.

Why it matters:
- Direct impact on cost  
- Efficiency of model responses  

---

### 2. Latency
Measures response time for each model.

Why it matters:
- User experience  
- Real-time system feasibility  

---

### 3. Response Quality
Manual / qualitative observation of:
- Relevance  
- Clarity  
- Completeness  

---

## Key Observations

- Different models show clear trade-offs between **speed and quality**  
- Lower latency models are not always the most concise  
- Token usage varies more than expected for similar prompts  
- Response style (verbose vs concise) significantly impacts token count  

---

## 📊 Evaluation Results

The experiment evaluated all three models using the same set of 10 questions, focusing on **token usage, cost, latency, and response quality**.

---

### 🔹 Mistral – `mistral-small-latest`

- **Token Usage:**  
  More than 60% of responses reached the maximum output limit of 1000 tokens, indicating a tendency toward more verbose outputs.

- **Cost:**  
  Total cost for all queries was approximately **$0.00255**, making it the most cost-efficient option in this comparison.

- **Latency:**  
  Most responses were generated within **6 to 8.5 seconds**, showing relatively stable and faster performance.

- **Response Quality:**  
  Around **70% of responses achieved a quality score of 5**, reflecting strong but slightly variable output quality.

---

### 🔹 OpenAI – `gpt-4o-mini`

- **Token Usage:**  
  Approximately 60% of responses were under **600 tokens**, indicating more concise and controlled responses.

- **Cost:**  
  Total cost was approximately **$0.00333**, slightly higher than Mistral.

- **Latency:**  
  Around 60% of responses took **more than 9 seconds**, with a few responses reaching up to **14 seconds**.

- **Response Quality:**  
  All responses consistently achieved a **quality score of 5**, demonstrating highly reliable performance.

---

### 🔹 Anthropic – `claude-sonnet-4-6`

- **Token Usage:**  
  About 50% of responses were under **500 tokens**, while a few responses reached the maximum limit of 1000 tokens, showing mixed verbosity.

- **Cost:**  
  Total cost for all queries was approximately **$0.00371**, the highest among the evaluated models.

- **Latency:**  
  Around 50% of responses took between **12 to 23 seconds**, indicating higher response times.

- **Response Quality:**  
  Approximately **80% of responses achieved a quality score of 5**, showing strong overall quality.

---

## 🧠 Summary Insights

- **Mistral** stands out for **cost efficiency and lower latency**, but tends to generate longer responses.  
- **GPT-4o-mini** provides the most **consistent response quality**, with more concise outputs.  
- **Claude Sonnet** delivers strong quality but at the cost of **higher latency and overall expense**.  

👉 Each model presents a different balance between **efficiency, speed, and quality**, making model selection highly dependent on the specific use case.

---

## Why This Experiment Matters

In real applications, choosing a model is not just about accuracy.

You need to balance:
- Cost (tokens)  
- Performance (latency)  
- Output usefulness (quality)  

---

## Possible Extensions

- Add automated scoring (LLM-as-judge)  
- Track cost per request  
- Increase dataset size  
- Introduce domain-specific queries  
- Visualize results (charts / dashboards)  

---

## How to Run

1. Clone the repo  
2. Set API keys for each provider  
3. Run the evaluation script  
4. Review output logs / results  

---

## Repo

https://github.com/TechTrojan/GenAI/tree/Cost_Lat_Eng

---

## Final Thought

This wasn’t about finding the “best” model.

It was about understanding how each model behaves under the same conditions — and that’s where real insights start.
