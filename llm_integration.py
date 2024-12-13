import openai

# Replace with your actual API key
openai.api_key = 'your_openai_api_key'

def interact_with_llm(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or another engine
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error interacting with LLM: {e}"
