'''
single source of truth for all configuration values.
Any module that needs API,model name,retry limits or path constants import from here
'''
import os
from pathlib import Path
from dotenv import load_dotenv

#project root directory
#Path(__file__): gives full path of the current file
# (config.py  
# in this case
#.parent: gives the directory containing the file, \
# which is the project root in this case
PROJECT_ROOT = Path(__file__).parent

#load environment variables from .env file atPROJECT_ROOT/.ENV into os.environment
load_dotenv(dotenv_path=PROJECT_ROOT / '.env')

GEMINI_API_KEY=os.getenv('api_key')

# DEFAULT_MODEL_NAME = 'models/gemini-2.5-flash'
DEFAULT_MODEL_NAME = 'gemini-2.5-flash'
#retry limits for API calls
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

#DATASET CONFIGURATION
DATASET_PATH = PROJECT_ROOT / 'scam_detection_dataset.csv'
TEST_DATASET = PROJECT_ROOT / 'test_scam_dataset.csv'

TEXT_COLUMNS = ['text', 'message_text','message']
LABEL_COLUMN = 'label'

#PATHS
OUTPUT_DIR=PROJECT_ROOT / 'outputs'
LOGS_DIR=PROJECT_ROOT / 'logs'

#cREATE OUTPUT DIRECTORIES IF THEY DONT EXIST
OUTPUT_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

def get_dataset_path(filename: str) -> Path:

    """

    Find dataset file in project directory.

    Args:

        filename: Name of the dataset file

    Returns:
        Path to the dataset file

    Raises:
        FileNotFoundError: If file not found

    """

    # Try direct path first

    if Path(filename).exists():

        return Path(filename)

    

    # Try project root

    project_path = PROJECT_ROOT / filename

    if project_path.exists():

        return project_path

    

    raise FileNotFoundError(f"Dataset '{filename}' not found")

