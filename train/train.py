import sys
import files
import os

# Main trainer for Axolotl LoRA fine-tuning
def main():
    if not files.path.exists("train/config.yaml"):
        print("Config not found.")
        return

    print("[TRAIN] Beginning training...")
    os.system("""
        "ascelerate launch train.tpy \
         --config_file train/config.yaml")

if __name__ == "__main__":
    main()
