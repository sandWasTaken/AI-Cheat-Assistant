
import os
import subprocess
import sys

# Check if config exists
if not os.path.exists("train/config.yaml"):
    print("[!] ERROR: config.yaml not found")
    sys.exit(1)

print("[\\TRAINING\\] Launching Axolotl Pipeline...")

# Run the actual Axolotl CLI training script
sys.argv = [
    "accelerate",
    "launch",
    "train/run_train.py",
    "--config_file",
    "train/config.yaml"
]

try:
    subprocess.run([sys.executable, "train/run_train.py", "--config_file", "train/config.yaml"])
    print("[SUCCESS] Training complete.")
    if not os.path.exists("train/output"):
        os.makedirs("train/output")
    print("[COMPLETE] Tuned model saved to train/output.")
except Exception:
    print(" [ERROR] Failed to run real training...")
    sys.exit(1)
