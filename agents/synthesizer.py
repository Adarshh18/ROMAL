import google.generativeai as genai
import time

def run_synthesizer(original_query: str, analysed: str, api_key: str) -> str:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""You are a Critique & Synthesis Agent. Review the analysis and write a final document.

Query: {original_query[:400]}
Analysis: {analysed[:600]}

Output:
1. Issues found (1-2 lines)
2. EXECUTIVE SUMMARY (2 sentences)
3. KEY FINDINGS (3 bullet points)
4. CONCLUSIONS (2 sentences)
5. LIMITATIONS (1 sentence)
Total: under 400 words."""

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
                return f"[Synthesizer Agent Error] {err}"
            return f"[Synthesizer Agent Error] {err}"
    return "[Synthesizer Agent Error] Rate limit reached after retries."