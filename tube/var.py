from pathlib import Path

PROJECT_ROOT = Path(__package__).absolute().parent
OUTPUT_DIR = Path(PROJECT_ROOT).joinpath('downloads')