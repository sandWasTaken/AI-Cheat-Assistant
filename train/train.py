import sys
import os

# Main training script for Axolotl LoRA
def main():
    if not os.path.exists("train/config.yaml"):
        print(" [ERROR] config.yaml not found ...")
        sys.stdout.write("Exiting...\n")
        return
    print("STARTING TRAINING".center())
    os.system("accelerate launch train/train.py --config_file train/config.yaml")
if __name__ == "__main__":
    main()
