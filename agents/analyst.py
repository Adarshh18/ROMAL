import google.generativeai as genai
import time

def run_analyst(original_query: str, decomposed: str, api_key: str) -> str:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""You are a Research Analyst. Analyze these sub-questions concisely.

Query: {original_query[:400]}
Sub-questions: {decomposed[:500]}

For each sub-question: key findings, concepts, current knowledge state.
Then: 2 hypotheses + 2 research gaps. Total: 350-450 words."""

    for attempt in range(3):
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(max_output_tokens=520)
            )
            return response.text.strip()
        except Exception as e:
            err = str(e)
            if "429" in err or "quota" in err.lower() or "RESOURCE_EXHAUSTED" in err:
                if attempt < 2:
                    time.sleep(20 * (attempt + 1))
                    continue
                return f"[Analyst Agent Error] {err}"
            return f"[Analyst Agent Error] {err}"
    return "[Analyst Agent Error] Rate limit reached after retries."