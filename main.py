import requests
import zipfile
import os

# URL of the GTFS zip file
url = 'https://ssl.renfe.com/gtransit/Fichero_AV_LD/google_transit.zip'

# Path to save the downloaded zip file
zip_path = 'google_transit.zip'
extract_path = 'google_transit_data'

# Download the zip file
response = requests.get(url)
with open(zip_path, 'wb') as file:
    file.write(response.content)

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# Clean up the zip file
os.remove(zip_path)
