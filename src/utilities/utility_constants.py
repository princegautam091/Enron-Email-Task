import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
generated_files_dir = os.path.join(ROOT_DIR, 'generated_files')
os.makedirs(generated_files_dir, exist_ok=True)
