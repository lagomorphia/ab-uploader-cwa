from dotenv import load_dotenv
from upload import ABUploader
load_dotenv()\
# Change these variables.

import requests
import csv
url = 'https://raw.githubusercontent.com/lodgepolepines/ab-uploader-cwa/main/ab_uploader_test.csv'
r = requests.get(url)
text = r.iter_lines()
upload_file = csv.reader(text, delimiter=',')

config_file = 'config.example.yml'
campaign_key = 'upload-test'
config = ABUploader.parse_config(config_file, campaign_key)
uploader = ABUploader(config, upload_file)
uploader.start_upload('people')
uploader.confirm_upload()
uploader.finish_upload()
uploader.quit()
