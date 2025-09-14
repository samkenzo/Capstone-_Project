import pandas as pd
import requests
from io import StringIO

# Download the correct SpaceX dataset
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv'

try:
    response = requests.get(url)
    spacex_df = pd.read_csv(StringIO(response.text))
    # Save locally
    spacex_df.to_csv("spacex_launch_dash.csv", index=False)
    print("CSV downloaded successfully!")
    print("Columns:", spacex_df.columns.tolist())
except Exception as e:
    print(f"Error downloading: {e}")
