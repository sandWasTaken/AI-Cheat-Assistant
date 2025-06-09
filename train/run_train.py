import sys
import os
from axolotl.cli import launch

# Check config.file exists
if not os.path.exists("train/config.yaml"):
    print("[!ERROR] config.yaml not found.")
    sys.exit(1)

print("[/TOP\\TRAINING/ ] Loading config.file and starting Axolotl training...")
launch()
