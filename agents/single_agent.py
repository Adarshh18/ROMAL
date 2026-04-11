import google.generativeai as genai
import time

def run_single_agent(query: str, api_key: str) -> str:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""You are a research assistant. Answer the question below clearly in 300-400 words.

Question: {query[:500]}"""

    for attempt in range(3):
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(max_output_tokens=480)
            )
            return response.text.strip()
        except Exception as e:
            err = str(e)
            if "429" in err or "quota" in err.lower() or "RESOURCE_EXHAUSTED" in err:
                if attempt < 2:
                    time.sleep(20 * (attempt + 1))
                    continue
                return f"[Single Agent Error] {err}"
            return f"[Single Agent Error] {err}"
    return "[Single Agent Error] Rate limit reached after retries."