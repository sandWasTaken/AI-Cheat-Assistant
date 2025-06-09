import sys
import os

# Main training script
def main():
    if not os.path.exists("train/config.yaml"):
        print("  ERROR : config.yaml not found ...")
        return
    print("STARTING TRAINING".center(50))
    os.system("accelerate launch train/run_train.py --config_file train/config.yaml")
if __name__ == "__main__":
    main()
