import sys
import os
from pathlib import Path

# Add the project directory to the sys.path
project_home = str(Path(__file__).resolve().parent)
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the environment variable for the Flask app
os.environ['FLASK_APP'] = 'app'

# Import the Flask app
from app import app as application
