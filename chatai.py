import os
from openai import OpenAI

class ChatOpenAI:
    api_key = ""

    def __init__(
        self,
        *,
        api_key: str = None,
        base_url: str = None,
        sys_prompt: str = "You are a good assistant, answer the question as best you can.",
        user_prompt: str = None,
        type: str = None,
        model: str = "gpt-3.5-turbo",
        temperature: float = 0.7):
        self.api_key = api_key
        self.base_url = base_url
        self.system_prompt = sys_prompt
        self.user_prompt = user_prompt
        self.model = model
        self.temperature = temperature

    def query_openai(self, text):
        content = ""
        client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url
        )
        completion = client.chat.completions.create(
            model= self.model,
            messages=[
                {"role": "system", "content":self.system_prompt},
                {"role": "user", "content":self.user_prompt+"\n"+text}
            ],
            temperature=self.temperature,
        )
        return completion.choices[0].message.content