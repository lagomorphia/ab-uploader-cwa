from dotenv import load_dotenv
from upload import ABUploader
import pandas as pd
load_dotenv()

import pandas as pd 
# intialise data
data = {'first_name':['Heather'],
'middle_name':['SELENIUM'], 'last_name':['Burroughs']} 
# Create DataFrame 
df = pd.DataFrame(data) 
df.to_csv('/app/ab_uploader_test.csv', index=False)

# Change these variables.
upload_file = '/app/ab_uploader_test.csv'
config_file = 'config.example.yml'
campaign_key = 'upload-test'
config = ABUploader.parse_config(config_file, campaign_key)
uploader = ABUploader(config, upload_file)
uploader.start_upload('people')
uploader.confirm_upload()
uploader.finish_upload()
uploader.quit()
