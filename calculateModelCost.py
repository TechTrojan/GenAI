import json
import pandas as pd

INPUT_FILE = "Keyword_Model_RouterResult.json"
OUTPUT_FILE = "Kyeword_Router.csv"

MODEL_PRICING = {
    "mistral-small-latest": {
        "input": 0.10,
        "output": 0.30
    },
    "mistral-medium-latest": {
        "input": 0.40,
        "output": 2.00
    },
    "gpt-4o-mini": {
        "input": 0.15,
        "output": 0.60
    },
    "gpt-4o": {
        "input": 2.50,
        "output": 10.00
    }
}


def calculate_cost(tokens, rate):
    return round((tokens / 1_000_000) * rate, 8)


with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []

for index, item in enumerate(data, start=1):

    router = item.get("routerMatrix", {})
    route = item.get("routerResponse", {})
    llm = item.get("llmResponse", {})

    router_price = MODEL_PRICING.get(
        router.get("model_name"),
        {"input": 0, "output": 0}
    )

    llm_price = MODEL_PRICING.get(
        llm.get("model_name"),
        {"input": 0, "output": 0}
    )

    router_input = calculate_cost(
        router.get("prompt_token", 0),
        router_price["input"]
    )

    router_output = calculate_cost(
        router.get("response_token", 0),
        router_price["output"]
    )

    router_total = round(
        router_input + router_output,
        8
    )

    llm_input = calculate_cost(
        llm.get("prompt_token", 0),
        llm_price["input"]
    )

    llm_output = calculate_cost(
        llm.get("response_token", 0),
        llm_price["output"]
    )

    llm_total = round(
        llm_input + llm_output,
        8
    )

    rows.append({
        "Sr.No": index,
        "Question": item.get("question"),

        "routerModel_name":
            router.get("model_name"),

        "routerSuggestedRoute":
            route.get("route"),

        "routerModel_Confidence":
            route.get("confidence"),

        "routerModel_Selection_Reason":
            route.get("reason"),

        "router_PromptToken":
            router.get("prompt_token"),

        "router_response_token":
            router.get("response_token"),

        "router_total_token":
            router.get("total_token"),

        "router_ResponseTime":
            router.get("total_response_time"),

        "router_inputcost":
            router_input,

        "router_outputcost":
            router_output,

        "router_totalcost":
            router_total,

        "llmModel_name":
            llm.get("model_name"),

        "llm_PromptToken":
            llm.get("prompt_token"),

        "llm_response_token":
            llm.get("response_token"),

        "llm_total_token":
            llm.get("total_token"),

        "llm_ResponseTime":
            llm.get("total_response_time"),

        "llm_inputcost":
            llm_input,

        "llm_outputcost":
            llm_output,

        "llm_totalcost":
            llm_total,

        "total_cost_each_question":
            round(
                router_total + llm_total,
                8
            ),

        "total_response_time_each_question":
            round(
                router.get(
                    "total_response_time",
                    0
                )
                +
                llm.get(
                    "total_response_time",
                    0
                ),
                6
            )
    })

df = pd.DataFrame(rows)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print(f"Generated: {OUTPUT_FILE}")
print(df.head())