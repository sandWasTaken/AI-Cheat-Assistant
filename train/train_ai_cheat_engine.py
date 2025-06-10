import json
import os

from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling

def load_data(path="data.json"):
    with open(path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
    return ["<prompt>: " + d["prompt"] + "\nresponse>: " + d["response"] for d in raw_data]

def main():
    dataset = load_data()
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    tokenizer.pad_token = tokenizer.eos_token
    model.resize_token_embeddings(len(tokenizer))

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
