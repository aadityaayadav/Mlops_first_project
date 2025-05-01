import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

list_of_files = [
    "github/workflows",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_training.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
]

for file in list_of_files:
    file_path = Path(file)  # ✅ Corrected this
    filedir, filename = os.path.split(file)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if not os.path.exists(file) or os.path.getsize(file) == 0:
        with open(file, 'w') as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {file}")
