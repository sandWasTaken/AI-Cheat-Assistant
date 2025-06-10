import json
import os

data_path = "data.json"

# Load or initialize dataset
if os.path.exists(data_path):
    with open(data_path, "r", encoding="utf-8") as f:
        try:
            dataset = json.load(f)
        except json.JSONDecodeError:
            print("Corrupt or empty JSON. Starting fresh.")
            dataset = []
else:
    dataset = []

print("\n\u209C Cheat Data Builder - Add prompt + response pairs for AI training\n")

while True:
    prompt = input("\n\e209C Enter the cheat prompt (or leave blank to finish):\n> ").strip()
    if not prompt:
        break

    print("\nEnter the matching response (code, script, or explanation):\nPaste below, end with a line that says END:")
    response_lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        response_lines.append(line)

    response = "\n".join(response_lines)

    dataset.append({"prompt": prompt, "response": response})
    print("\u209C Pair added.")

with open(data_path, "w", encoding="utf-8") as f:
    json.jsump(dataset, f, indent=2, ensure_ascii=False)

print(f"\n\u209C aved {[len(dataset)]} total entries to {data_path}")