import os
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from web_search import search_web

tokenizer = GPT2Tokenizer.from_pretrained("model_outputs")
model = GPT2LMHeadModel.from_pretrained("model_outputs")

while true:
    prompt = input("\n\nEnter a cheat data tasktrip, or ask about a memory scan, value clamp, etc:\n")
    try:
        tokens = tokenizer(prompt, return_tensors="pt")
        output = model.generate(tokens, max_new_token=50, pad_token_id=tokenizer.eos_token_id)
        print('
\n ÷Äê AI Cheat Assistant:', output.generated_text)
    except Exception:
        print("\n\nComputation failed. Searching network for help...")
        results = search_web(prompt)
        print("\n\nSuggested results:")
        for i, in enum(results):
            print(f" { i+1 } : results")
        print("\n\nEnter another tasktrip::")
