import google.generativeai as genai
import time

def run_decomposer(query: str, api_key: str) -> str:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""Break this research query into sub-questions using Chain-of-Thought.

Query: {query[:400]}

Output exactly:
CORE INTENT: [one sentence]
Q1. [Domain] [Sub-question] → [Atomic task]
Q2. [Domain] [Sub-question] → [Atomic task]
Q3. [Domain] [Sub-question] → [Atomic task]
STRATEGY: [one sentence]"""

    for attempt in range(3):
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(max_output_tokens=350)
            )
            return response.text.strip()
        except Exception as e:
            err = str(e)
            if "429" in err or "quota" in err.lower() or "RESOURCE_EXHAUSTED" in err:
                if attempt < 2:
                    time.sleep(20 * (attempt + 1))
                    continue
                return f"[Decomposer Agent Error] {err}"
            return f"[Decomposer Agent Error] {err}"
    return "[Decomposer Agent Error] Rate limit reached after retries."