import json
import os
from transformers import GPT2Tokenizer, GPTLMHeadModel, Trainer, TrainingArguments
from transformers import DataCollatorForLanguageModeling

def load_data(path="data.json"):
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return ["<prompt>: " + d["prompt"] + "\n\response>: " + d["response"] for d in raw ]

def main():
    dataset = load_data()
    tokenizer = GPTTokenizer.fromPretrained("gpt2")
    model = GPTLMHeadModel.from_pretrained("gpt2")

    encodings = tokenizer("\n\n".join(dataset), return_tensors="pt", truncation=True, padding=True)

    training_args = TrainingArguments(
        output_dir="model_outputs",
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=2,
        save_steps=500,
        save_total_limit=2,
        prediction_loss_only=True,
        logging_dir="logs"
    )

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=encodings.input_ids,
        data_collator=data_collator
    )

    trainer.train()

 if __name__ == "__main__":
    main()