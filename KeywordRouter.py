from ModelRouterResponse import RouterResponse
from pydantic import BaseModel
import re

class KeywordRouter(BaseModel):
    DEFAULT_ROUTE:str  = "Quality"
    
    
    PRIORITY_ORDER : list [str] = [
    "Code",
    "Quality",
    "Simple"
]
    
    ROUTER_KEYWORDS  : list = {
    "Code": [
        # code generation
        "code",
        "python",
        "java",
        "javascript",
        "typescript",
        "c++",
        "c#",
        "golang",
        "sql",
        "bash",
        "script",
        "function",
        "class",
        "method",
        "api",
        "sdk",
        "library",
        "framework",
        "implementation",
        "algorithm",

        # coding actions
        "generate code",
        "write code",
        "create code",
        "implement",
        "build api",
        "develop",
        "refactor",
        "optimize code",
        "convert code",

        # debugging / troubleshooting
        "debug",
        "fix",
        "error",
        "exception",
        "traceback",
        "bug",
        "issue",
        "problem in code",
        "runtime error",
        "syntax error",
        "stack trace",

        # development tooling
        "git",
        "docker",
        "kubernetes",
        "pipeline",
        "ci/cd",
        "deployment",
        "yaml",
        "json",
        "csv",
        "database",
        "query",
        "endpoint",
        "microservice",

        # AI engineering coding
        "langchain",
        "rag pipeline",
        "vector db",
        "embedding",
        "openai api",
        "prompt template",
        "agent",
        "tool calling"
    ],

    "Quality": [
        # architecture / design
        "architecture",
        "system design",
        "design",
        "workflow",
        "framework",
        "platform",
        "infrastructure",
        "enterprise",
        "scalable",
        "production-ready",
        "high level design",

        # reasoning / analysis
        "compare",
        "comparison",
        "tradeoff",
        "trade-offs",
        "analyze",
        "analysis",
        "evaluate",
        "evaluation",
        "pros and cons",
        "advantages and disadvantages",
        "best approach",
        "recommendation",
        "strategy",

        # AI / LLM concepts
        "rag",
        "fine-tuning",
        "agentic ai",
        "multi-agent",
        "llmops",
        "prompt engineering",
        "model routing",
        "orchestration",
        "guardrails",
        "observability",
        "hallucination",
        "latency optimization",
        "cost optimization",

        # business / planning
        "roadmap",
        "planning",
        "decision",
        "governance",
        "security",
        "compliance",
        "risk",
        "optimization",

        # deep explanations
        "detailed explanation",
        "deep dive",
        "in detail",
        "real-world example",
        "case study",
        "research",
        "insights"
    ],

    "Simple": [
        # basic questions
        "what is",
        "what are",
        "who is",
        "define",
        "meaning",
        "overview",
        "introduction",

        # lightweight requests
        "summarize",
        "summary",
        "short explanation",
        "simple explanation",
        "in simple terms",
        "quick explanation",

        # list / tips
        "list",
        "examples",
        "tips",
        "benefits",
        "advantages",
        "features",
        "use cases",

        # writing tasks
        "linkedin post",
        "email",
        "message",
        "caption",
        "headline",
        "hashtags",

        # recommendations
        "recommend",
        "suggest",
        "best",
        "top",
        "ideas",

        # beginner-friendly
        "beginner",
        "easy",
        "basic",
        "simple",
        "starter"
    ]
}
    
    
    

    def contains_keyword(self, text: str, keyword: str) -> bool:
        pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
        return re.search(pattern, text.lower()) is not None
        
    def single_question(self,question: str) -> RouterResponse:
        q = question.lower()
        response=RouterResponse( route=self.DEFAULT_ROUTE, confidence= 0.5, reason= f"No keyword matched. Defaulted to Quality route.") 

        for route in self.PRIORITY_ORDER:
            for keyword in self.ROUTER_KEYWORDS[route]:
                if self.contains_keyword(question, keyword):
                    response =  RouterResponse( route=route, confidence= 1.0, reason= f"Matched keyword: '{keyword}'") 
                    return response
                    

        return  response
        
        