# 🚀 Prompt Compression Experiment (OpenAI)

## 📌 Overview

This experiment evaluates the impact of **Prompt Compression** on:

- 💰 Token Usage  
- ⚡ Response Time (Latency)  
- 🧠 Response Quality  

Using **OpenAI (gpt-4o-mini)** as the model, we compare:

1. **Regular Prompts (Verbose)**
2. **Compressed Prompts (Optimized)**

---

## 🎯 Objective

To answer a key question:

> Can we reduce token usage and latency **without significantly impacting response quality?**

---


## 🧠 Architecture Diagram

<p align="center">
  <img src="./assets/images/architecture.png" alt="Architecture Diagram" width="900"/>
</p>

---

## 🧪 Experiment Setup

### 🔹 Model Used
- OpenAI: `gpt-4o-mini`

---

### 🔹 Test Dataset
- 10 prompts (verbose format)
- Each prompt tested in:
  - Regular (original)
  - Compressed version

---

### 🔹 Metrics Collected

| Metric | Description |
|------|-------------|
| Prompt Tokens | Tokens used in input |
| Completion Tokens | Tokens generated in output |
| Total Tokens | Sum of input + output |
| Response Time (ms) | Time taken for model response |
| Response Quality | LLM-evaluated score (1–5) |

---

## 📂 Result Files

- OpenAI_result_Regular.csv
- OpenAI_result_compressed.csv

---

## 📊 Sample Data Format

Prompt,PromptTokens,CompletionTokens,TotalTokens,Latency(ms),QualityScore
"Explain cloud computing...",120,180,300,850,4.5

---

## 🔬 Experiment Flow

Input Prompt (Verbose)
        ↓
Prompt Compression (Manual / LLM)
        ↓
Send to OpenAI Model
        ↓
Capture Response
        ↓
Measure:
   - Token Usage
   - Latency
   - Response
        ↓
Evaluate Quality (LLM Judge)
        ↓
Store Results (CSV)

---

## 📈 Key Comparisons

| Comparison | Goal |
|----------|------|
| Regular vs Compressed | Token reduction |
| Latency difference | Performance gain |
| Quality score | Impact on output |

---

## 🧠 Expected Insights

- Reduced tokens → lower cost  
- Faster responses with shorter prompts  
- Minimal or controlled drop in quality  
- Optimal balance between efficiency and accuracy  

---

## 💡 Key Takeaway

Prompt design is one of the most powerful levers to optimize cost, latency, and performance in LLM applications.

---

## 🛠️ Technologies Used

- Python  
- OpenAI API (`gpt-4o-mini`)  
- CSV / JSON  

---

Nice — this is where your experiment becomes **valuable insight**, not just data.

Here’s a **clean, README-ready summary section** based on your actual results 👇

---

## 📊 Key Insights from Experiment

### 🔹 1. Token Usage Optimization

* **Regular Prompts (Avg Total Tokens):** ~536
* **Compressed Prompts (Avg Total Tokens):** ~527

👉 **~1.5–2% reduction in total tokens**

💡 Insight:

> Prompt compression reduces token usage, but the impact depends on how aggressively prompts are compressed. In this experiment, moderate compression led to small but consistent savings.

---

### ⚡ 2. Response Time (Latency)

* **Regular Prompts Avg Latency:** ~7.75 sec
* **Compressed Prompts Avg Latency:** ~7.60 sec

👉 Slight improvement (~2% faster)

💡 Insight:

> Shorter prompts slightly improve response time, but latency is influenced more by **output size and model processing** than input size alone.

---

### 🧠 3. Response Quality Improvement

* **Regular Avg Quality Score:** 4.12
* **Compressed Avg Quality Score:** 4.35

👉 **Quality improved (~5–6%)**

💡 Insight:

> Prompt compression did **not degrade quality** — in fact, it improved clarity and usefulness in many cases by removing unnecessary verbosity.

---

### ⚖️ 4. Clarity & Completeness Tradeoff

* **Clarity improved** (4.1 → 4.4)
* **Completeness improved** (3.3 → 3.6)

💡 Insight:

> Structured and concise prompts help the model produce **more focused and complete answers**, avoiding noise from overly verbose instructions.

---

### 🔍 5. Variability Observed

* Compressed prompts showed:

  * **Higher variance in tokens**
  * Some cases with **higher token usage (up to 620)**

💡 Insight:

> Compression is not always linear — poorly compressed prompts can **increase output verbosity**, leading to higher token usage.

---

## 🏆 Final Conclusion

> Prompt Compression is a **high-leverage optimization technique** that can improve efficiency without sacrificing quality.

### ✅ Benefits Observed:

* Slight reduction in token usage
* Slight improvement in latency
* Noticeable improvement in response quality

### ⚠️ Considerations:

* Compression strategy matters
* Over-compression can lead to inconsistent outputs
* Best results come from **structured + intentional prompts**

---

## 🚀 Key Takeaway

> The best prompts are not the shortest — they are the **most efficient per token**.


---

## 🚀 Future Enhancements

- Multi-model comparison  
- Automated compression pipeline  
- Visualization dashboards  
- Cost analysis  

---

## 📚 Top References

1. **OpenAI Prompt Engineering Guide**
   [https://platform.openai.com/docs/guides/prompt-engineering](https://platform.openai.com/docs/guides/prompt-engineering)

2. **OpenAI Pricing (Token Cost Understanding)**
   [https://platform.openai.com/docs/pricing](https://platform.openai.com/docs/pricing)

3. **Anthropic Prompt Engineering (Excellent for Structured Prompts)**
   [https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)

4. **Microsoft Prompt Engineering Guide (Enterprise Perspective)**
   [https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)

5. **Prompting Techniques for Large Language Models (Research Paper)**
   [https://arxiv.org/abs/2302.11382](https://arxiv.org/abs/2302.11382)


---

## 📬 Feedback

Feel free to contribute or share feedback!
