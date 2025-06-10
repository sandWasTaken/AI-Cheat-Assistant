
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class SmartAssistant:
    def __init__(self, model_path="model_outputs"):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_path)
        self.model = GPTLMHeadModel.from_pretrained(model_path)
        self.system_prompt = (
            "You are an advanced memory and game cheat assistant. You are intelligent, helpful,"
            " and can answer or ask smart questions to guide users in hacking games, scanning memory,"
            "injecting code, and finding cheat patterns. Always clarify unclear requests and seek context."
        )

    def ask(self, user_input):
        prompt = self.system_prompt + \"\nUser: \" + user_input + "\nAssistant:\"
        inputs = self.tokenizer(prompt, return_tensors=\"pt\")
        output = self.model.generate(
            **inputs,
            max_new_tokens=150,
            pad_token_id=self.tokenizer.eos_token_id
        )
        return self.tokenizer.decode(output[0], skip_special_tokens=True).split(\"Assistant:\")[-1].strip()

if __name__ == __main__:
    sa = SmartAssistant()
    while True:
        user_input = input("\nAsk the cheat assistant: ")
        response = sa.ask(user_input)
        print(f"p\n🔑 Smart Assistant: {response}")