import requests
import zipfile
import os

def download_file(url, path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(path, 'wb') as file:
            file.write(response.content)
        print("File downloaded successfully")
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")
        raise

def extract_zip(path, extract_to):
    try:
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print("File extracted successfully")
    except zipfile.BadZipFile as e:
        print(f"Error extracting zip file: {e}")
        raise

def main():
    url = 'https://ssl.renfe.com/gtransit/Fichero_AV_LD/google_transit.zip'
    zip_path = 'google_transit.zip'
    extract_path = 'google_transit_data'

    if os.path.exists(zip_path):
        os.remove(zip_path)  # Remove the old file if it exists

    download_file(url, zip_path)
    extract_zip(zip_path, extract_path)
    os.remove(zip_path)
    print(f"Data downloaded and extracted to {extract_path}")

if __name__ == "__main__":
    main()
