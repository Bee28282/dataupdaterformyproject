{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import requests\
import zipfile\
import os\
import io\
\
GTFS_URL = "{\field{\*\fldinst{HYPERLINK "https://ssl.renfe.com/gtransit/Fichero_AV_LD/google_transit.zip"}}{\fldrslt https://ssl.renfe.com/gtransit/Fichero_AV_LD/google_transit.zip}}"  # Replace with actual GTFS dataset URL\
OUTPUT_DIR = "data"  # Directory to save the unzipped files\
\
def download_gtfs(url):\
    print(f"Downloading GTFS data from \{url\}...")\
    response = requests.get(url)\
    response.raise_for_status()  # Ensure we notice bad responses\
    return response.content\
\
def unzip_gtfs(data, output_dir):\
    print(f"Unzipping GTFS data to \{output_dir\}...")\
    with zipfile.ZipFile(io.BytesIO(data)) as z:\
        z.extractall(output_dir)\
    print(f"Files extracted to \{output_dir\}")\
\
def main():\
    data = download_gtfs(GTFS_URL)\
    os.makedirs(OUTPUT_DIR, exist_ok=True)\
    unzip_gtfs(data, OUTPUT_DIR)\
\
if __name__ == "__main__":\
    main()}