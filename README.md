# Smart Model Router: Cost-Aware LLM Routing Experiment

## Overview

This experiment explores a practical question in AI application design:

> Can a lightweight router model reduce overall LLM cost by sending simpler questions to cheaper models while keeping more complex/code-related questions on stronger models?

Instead of sending every user question to the same baseline model, this experiment introduces a **Smart Model Router**. The router first analyzes the user question, classifies it into a route, and then selects the final LLM based on that route.

The experiment compares:

* **Baseline approach:** all questions go directly to `gpt-4o`
* **Router approach:** questions first go to a router model, then to the selected final model

The goal is not only to compare cost and response time, but also to understand whether the router makes correct routing decisions.

---

## Experiment Design

The experiment uses a mixed workload of **40 questions** covering three types of tasks:

* Simple explanation / short writing tasks
* Quality-focused architecture, comparison, and reasoning tasks
* Code generation and debugging tasks

The router model returns a structured JSON response with:

```json
{
  "route": "Simple | Quality | Code",
  "confidence": 0.95,
  "reason": "Reason for selecting this route"
}
```

---

## Architecture Diagram


<p align="center">
  <img src="./assets/images/architecture.png" alt="Architecture Diagram" width="900"/>
</p>
---

## How the Model Router Works

The main routing logic is implemented in `ModelRouter.py`.

### Route-to-model mapping

```python
Simple  -> gpt-4o-mini
Quality -> gpt-4o-mini
Code    -> gpt-4o
```

### Why this mapping matters

The baseline sends all 40 questions to `gpt-4o`.

The router approach sends:

* Simple questions to `gpt-4o-mini`
* Quality questions to `gpt-4o-mini`
* Code questions to `gpt-4o`

This means **29 out of 40 questions** are routed to the lower-cost model, while only code-heavy questions stay on `gpt-4o`.

---

## Evaluation Flow

1. Prepare the same set of 40 questions.
2. Run all questions through the baseline model: `gpt-4o`.
3. Run the same questions through the model router.
4. Router model classifies each question into one route.
5. Final LLM is selected based on route.
6. Capture metrics for both router model and final LLM.
7. Compare baseline vs router approach.

---

## Metrics Captured

### Cost metrics

* Router model input cost
* Router model output cost
* Router model total cost
* Final LLM input cost
* Final LLM output cost
* Final LLM total cost
* Total cost per question
* Total experiment cost

### Latency metrics

* Router response time
* Final LLM response time
* Total response time per question
* Total experiment response time

### Router quality metrics

* Route accuracy
* Route distribution
* Router confidence
* Model selection correctness
* Router reason for each decision

---

## Result Summary

### Route distribution

| Route     | Question Count |
| --------- | -------------: |
| Simple    |             18 |
| Quality   |             11 |
| Code      |             11 |
| **Total** |         **40** |

### Router evaluation metrics

| Metric                      | Result |
| --------------------------- | -----: |
| Route Accuracy              |   100% |
| Average Router Confidence   |  95.8% |
| Model Selection Correctness |   100% |

### Cost comparison

| Approach                            | Total Cost |
| ----------------------------------- | ---------: |
| Baseline: all questions to `gpt-4o` |   $0.18107 |
| Router model cost                   |   $0.00535 |
| Final LLM cost after routing        |   $0.05852 |
| Router experiment total cost        |   $0.06388 |

### Cost savings

```text
Cost savings = Baseline cost - Router experiment cost
             = $0.18107 - $0.06388
             = $0.11719 saved
```

The router approach reduced total cost by approximately:

```text
64.7% lower cost compared to baseline
```

---

## Response Time Comparison

| Approach                            | Total Response Time |
| ----------------------------------- | ------------------: |
| Baseline: all questions to `gpt-4o` |          160.03 sec |
| Router approach                     |          340.10 sec |

### Latency impact

The router approach was slower by:

```text
+180.07 sec
+112.5% slower than baseline
```

This happened because every request first passes through the router model before calling the final selected LLM.

---

## Key Findings

### 1. The router reduced cost significantly

The router saved cost because most questions did not need the expensive baseline model.

In this experiment:

* 29 questions were served by `gpt-4o-mini`
* 11 code-related questions were served by `gpt-4o`

This routing strategy reduced total cost by **64.7%** compared to sending all questions directly to `gpt-4o`.

---

### 2. Router overhead was small in cost

The router model added extra cost, but the router cost was small compared to the savings from using `gpt-4o-mini` for Simple and Quality routes.

```text
Router total cost: $0.00535
Final LLM total cost: $0.05852
Total routed cost: $0.06388
```

The router cost did not eliminate the savings.

---

### 3. Router overhead increased latency

The main tradeoff was response time.

The routed approach requires two model calls:

1. Router model call
2. Final LLM call

That extra step increased total response time from **160.03 sec** to **340.10 sec**.

So the router design is cost-efficient, but not latency-efficient in the current version.

---

### 4. Route accuracy and model selection were strong

The router selected the expected route for all 40 questions.

```text
Route Accuracy: 100%
Model Selection Correctness: 100%
Average Router Confidence: 95.8%
```

This shows that the routing logic worked well for the test dataset.

---

## Important Tradeoff

This experiment shows a common production AI tradeoff:

| Goal                         | Result         |
| ---------------------------- | -------------- |
| Reduce cost                  | Successful     |
| Preserve routing correctness | Successful     |
| Improve latency              | Not successful |

The router is useful when cost optimization is more important than lowest possible latency.

For real-time chat experiences, latency needs additional optimization.

---

## What I Would Improve Next

### 1. Reduce router latency

Possible improvements:

* Use a smaller/faster classifier model
* Use rule-based routing for obvious cases
* Cache router decisions for repeated prompts
* Run router with very low max tokens
* Use prompt caching for repeated router instructions

---

### 2. Add fallback logic

Example:

```python
if router_confidence < 0.85:
    selected_model = "gpt-4o"
```

This protects quality when the router is unsure.

---

### 3. Add quality scoring

Cost savings are useful only if response quality stays acceptable.

Future evaluation should include:

* Relevance
* Clarity
* Completeness
* Usefulness
* Technical correctness
* Overall quality score

---

### 4. Compare multiple routing strategies

Useful future comparison:

| Strategy            | Mapping                                                       |
| ------------------- | ------------------------------------------------------------- |
| Baseline            | All questions -> `gpt-4o`                                     |
| Cost-aware Router   | Simple/Quality -> `gpt-4o-mini`, Code -> `gpt-4o`             |
| Conservative Router | Simple -> `gpt-4o-mini`, Quality/Code -> `gpt-4o`             |
| Aggressive Router   | Simple/Quality/Code -> cheaper model unless confidence is low |

---

## How to Run

1. Clone the repository.
2. Switch to the `Model_Router` branch.
3. Configure API keys for OpenAI and Mistral.
4. Run the baseline experiment.
5. Run the router experiment.
6. Compare generated CSV files.

```bash
git clone https://github.com/TechTrojan/GenAI.git
cd GenAI
git checkout Model_Router
```

---

## Output Files

The experiment generates result files such as:

* `Baseline_model_version2_with_cost.csv`
* `model_router_question_costs.csv`
* `RouterResult_gpt4o_mini_quality.json.json`

These files are used to compare:

* Cost per question
* Response time per question
* Router route
* Router confidence
* Router reasoning
* Final selected model

---

## Final Takeaway

The Smart Model Router successfully reduced cost by routing most questions to a cheaper model while keeping code-related questions on a stronger model.

The main learning is:

> Model routing can reduce cost, but it introduces routing overhead. A good production design should optimize both cost and latency, not just one metric.

This experiment is a practical starting point for building cost-aware AI systems where different prompt types are handled by different models based on complexity, confidence, and expected quality.
