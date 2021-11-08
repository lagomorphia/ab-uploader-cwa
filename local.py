from dotenv import load_dotenv
from upload import ABUploader

load_dotenv()
# Change these variables.
upload_file = 'ab_uploader_test.csv' # path to test CSV
config_file = 'config.example.yml'
campaign_key = 'upload-test'
config = ABUploader.parse_config(config_file, campaign_key)
uploader = ABUploader(config, upload_file)
uploader.start_upload('people')
uploader.confirm_upload()
uploader.finish_upload()
uploader.quit()
