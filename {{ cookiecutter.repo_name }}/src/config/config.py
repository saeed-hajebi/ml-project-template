import pathlib
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent

## models
TRAINED_MODEL_DIR = PROJECT_ROOT / 'models'
DATASET_DIR = PROJECT_ROOT / 'data'

## data
TESTING_DATA_FILE = DATASET_DIR / 'processed/train'
TRAINING_DATA_FILE =  DATASET_DIR / 'processed/test'
TARGET = ''

# print(*[sys.path, PROJECT_ROOT, TESTING_DATA_FILE, TRAINING_DATA_FILE], sep='\n')

## variables
FEATURES = []
FEATURES_FINAL = []         # Final feature to keep in data
FEATURES_NUMERICAL = []     # Numerical
FEATURES_CATEGORICAL = []   # Categorical
FEATURES_TO_ENCODE = []     # Features to Encode
FEATURES_TEMPORAL = []      # Temporal (date/time)
FEATURES_LOG = []           # Features for Log Transform
FEATURES_DROP = []          # Features to Drop