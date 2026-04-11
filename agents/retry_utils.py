import time
import re
import google.generativeai as genai


def call_gemini_with_retry(prompt: str, api_key: str, max_retries: int = 4, base_delay: float = 40.0) -> str:
    """
    Call the Gemini API with smart retry on rate-limit (429) errors.
    
    Parses the "retry in X seconds" value from the API error when available,
    otherwise uses exponential backoff starting at 40s.
    """
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    last_error = None
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            last_error = e
            error_str = str(e)
            # Check if it's a rate limit error (429)
            is_rate_limit = ("429" in error_str or 
                           "quota" in error_str.lower() or 
                           "rate" in error_str.lower() or
                           "resource" in error_str.lower())
            
            if is_rate_limit and attempt < max_retries - 1:
                # Try to parse the suggested retry delay from the error message
                # e.g. "Please retry in 34.995114611s"
                retry_match = re.search(r'retry\s+(?:in|after)\s+([\d.]+)\s*s', error_str, re.IGNORECASE)
                if retry_match:
                    delay = float(retry_match.group(1)) + 2  # Add 2s buffer
                else:
                    delay = base_delay * (1.5 ** attempt)  # 40, 60, 90, 135s
                
                time.sleep(delay)
                continue
            elif not is_rate_limit:
                # Non-rate-limit error, don't retry
                raise e
    
    raise last_error
