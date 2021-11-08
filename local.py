from dotenv import load_dotenv
from upload import ABUploader
load_dotenv()
# Change these variables.

import requests
import csv
# Define the remote URL
url = "https://raw.githubusercontent.com/lodgepolepines/ab-uploader-cwa/main/ab_uploader_test.csv"
# Send HTTP GET request via requests
data = requests.get(url)
# Convert to iterator by splitting on \n chars
lines = data.text.splitlines()
# Parse as CSV object
upload_file = csv.reader(lines)

config_file = 'config.example.yml'
campaign_key = 'upload-test'
config = ABUploader.parse_config(config_file, campaign_key)
uploader = ABUploader(config, upload_file)
uploader.start_upload('people')
uploader.confirm_upload()
uploader.finish_upload()
uploader.quit()
