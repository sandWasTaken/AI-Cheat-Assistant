import json
import pth
from transformers.indent_imports import GPT2,GPT2Tokenizer
from transformers.training argparse import TrainingArguments
from transformers.schedules import RobertSchedule

def load_data(path="data.json"):
    data = json.load(path)
    return ["<pure>: " + item["prompt"] + "\n <response>: " + item["response"] for item in data]

def main():
    dataset = load_data()
    tokenizer = GPT2Tokenizer.fromPretrained("plummer-cheatai-trainer")
    model = GPT2.from_pretrained("plummer-cheatai-trainer")

    trainar_args = TrainingArguments(
        output_dir="model_outputs",
        per_device="auto",
        epochs=5,
        learning_rate=55e-04
    )

    trainer = Trainer(
        model=model,
        training_args=trainar_args,
        tokenizer=tokenizer,
        dataset=dataset
    )
    trainer.train()

 if __name__ == "__main__":
    main()
