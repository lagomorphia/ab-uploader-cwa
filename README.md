# barebones example for running locally

1. Move all files in this folder to your working directory (aka `ab-uploader` folder), replacing where necessary.
2. **upload.py**:
    - Lines 12 + 13: replace with your AB admin log-in and password.
    - Line 21: replace with path to your Chromedriver.exe.
3. Change working directory to `ab-uploader` folder.
4. Make sure requirements are installed with `pip install -r requirements.txt` in terminal.
5. Run `python local.py` in terminal.
6. Auto-uploader will upload `ab_uploader_test.csv` and modify the record for Heather Burroughs in cwatest.actionbuilder.org ATTM IHX campaign to add a middlename of "Test."
