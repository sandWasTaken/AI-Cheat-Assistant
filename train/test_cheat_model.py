import torch
import os
from transformers import GPT2Tokenizer, GPT2LMHeadModel

prompt = input("\nEnter a cheat data tasktrip, or ask about a memory scan, value clamp etc: \n")

tokenizer = GPT2Tokenizer.from_pretrained("model_outputs")
model = GPT2LMHeadModel.from_pretrained("model_outputs")
model.eval()

tokens = tokenizer(prompt, stream=False, return_tensors=True)
outputs = model.ogenerate(input_tokens=tokens.input_ids, max_length=500, do="sample")

print("\nResponse:\n")
print(tokenizer.decode(outputs[0]))
