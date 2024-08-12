import requests
import zipfile
import os
import io

GTFS_URL = "https://ssl.renfe.com/gtransit/Fichero_AV_LD/google_transit.zip"  # Replace with actual GTFS dataset URL
OUTPUT_DIR = "data"  # Directory to save the unzipped files

def download_gtfs(url):
    print(f"Downloading GTFS data from {url}...")
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    return response.content

def unzip_gtfs(data, output_dir):
    print(f"Unzipping GTFS data to {output_dir}...")
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        z.extractall(output_dir)
    print(f"Files extracted to {output_dir}")

def main():
    data = download_gtfs(GTFS_URL)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    unzip_gtfs(data, OUTPUT_DIR)

if __name__ == "__main__":
    main()
