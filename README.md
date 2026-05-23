# Smart LLM Routing: Comparing Default, Router LLM, and Keyword-Based Selection

## Overview

This experiment evaluates three approaches for selecting LLMs and measures the tradeoff between routing intelligence, cost optimization, and response latency.

Compared approaches:

1. Default Model (No Router)
2. Router Model (Small LLM performs routing)
3. Keyword Router (Rule-based routing)

Objective:

Reduce cost while maintaining acceptable response quality.

> Can routing intelligence reduce cost without reducing response quality?

---

## Experiment Design

| Component | Value |
|---|---|
| Framework | Python + LangChain |
| Routing Strategies | Default / Router / Keyword |
| Evaluation Dataset | Shared question set |
| Metrics | Cost, Latency, Tokens, Confidence |
| Evaluation Type | Comparative Experiment |

---

## Architecture Diagram

<p align="center">
  <img src="./assets/images/architecture.png" alt="Architecture Diagram" width="900"/>
</p>

---

## How It Works

1. Load evaluation dataset
2. Execute baseline model
3. Execute Router LLM flow
4. Execute Keyword Router flow
5. Capture metrics
6. Compare outputs
7. Generate experiment insights

---

## Evaluation Flow

Question Dataset  
↓  
Default Model Execution  
↓  
Router Model Execution  
↓  
Keyword Router Execution  
↓  
Metrics Aggregation  
↓  
Comparison Results  

---

## Metrics Captured

| Category | Metrics |
|---|---|
| Cost | Total Cost |
| Latency | Total Response Time |
| Tokens | Total Tokens |
| Routing | Router Confidence |
| Selection | Model Selection Correctness |

---

# Results Summary

## Performance Comparison

| Metric | Default | Router Model | Keyword Router |
|---|---:|---:|---:|
| Total Cost | $0.35149 | $0.14962 | $0.17824 |
| Total Response Time | 186.31 sec | 389.09 sec | 287.49 sec |
| Total Tokens | 18,059 | 52,309 | 18,856 |
| Routing Confidence | N/A | 97.27% | ~96% |

---

## Cost Comparison

| Approach | Cost Reduction |
|---|---:|
| Router Model | 57.4% |
| Keyword Router | 49.3% |

---

## Latency Comparison

| Approach | Increase vs Default |
|---|---:|
| Router Model | +108.8% |
| Keyword Router | +54.3% |

---

## Token Comparison

| Approach | Token Change |
|---|---:|
| Router Model | +189.7% |
| Keyword Router | +4.4% |

---

# Key Findings

## 1. Router Model achieved the strongest cost reduction

The Router Model delivered the lowest overall cost.

Why:
- Questions were dynamically routed to more appropriate models.
- Expensive model usage was reduced.

Business impact:
- Lower infrastructure spend

Technical impact:
- Additional inference overhead

---

## 2. Keyword Router delivered the strongest balance

Keyword routing reduced cost substantially while keeping routing confidence close to the Router Model.

Why:
- Routing decisions were deterministic.
- No additional router model execution.

Business impact:
- Lower operational complexity

Technical impact:
- Predictable routing behavior

---

## 3. Default execution remained fastest

Direct execution removed routing overhead and produced the lowest latency.

Business impact:
- Better responsiveness

Technical impact:
- Higher overall cost

---

# Tradeoffs

| Goal | Default | Router | Keyword |
|---|---|---|---|
| Cost | Weak | Best | Strong |
| Latency | Best | Weak | Moderate |
| Complexity | Best | High | Moderate |
| Predictability | Moderate | Moderate | Best |
| Scalability | Moderate | Strong | Strong |

---

# What I Would Improve Next

## 1. Hybrid Routing
Keyword → Router → Final LLM

---

## 2. Confidence-Based Fallback

```python
if confidence < 0.85:
    selected_model = stronger_model
```

---

## 3. Dynamic Cost-Aware Routing

Select model using:

- Estimated cost
- Latency threshold
- Quality requirements

---

## 4. Add Automated Quality Evaluation

Future dimensions:

- Relevance
- Clarity
- Completeness
- Usefulness

---

# How to Run

```bash
git clone https://github.com/TechTrojan/GenAI.git

cd Keyword_Router

python main.py
```

---

# Output Files

| File | Purpose |
|---|---|
| Baseline Results | Baseline execution |
| Router Results | Router evaluation |
| Keyword Results | Keyword evaluation |
| Comparison Report | Final metrics |

---

# Final Takeaway

This experiment shows that routing is not simply about choosing the strongest model.

The more practical challenge is selecting the right model for the right question while balancing:

- Cost
- Latency
- Routing confidence
- Operational simplicity

The Router Model achieved the lowest cost.

The Keyword Router delivered the strongest balance between efficiency and predictability.

The Default approach remained the fastest execution path.