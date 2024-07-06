# repoB/main.py
from pathlib import Path
import sys

# Adding path to the unified project root
sys.path.append(str(Path(__file__).resolve().parents[1]))

from config_loader import load_config

config = load_config()

if config['run_localhost']:
    print("Error: run_localhost is set to True")
