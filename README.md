# PDF Compression Script

This script compresses PDF files in a specified folder to a specific. 
It uses the `PyMuPDF` and `Pillow` library to handle PDF compression.

## Requirements

- Python 3.x
- `PyMuPDF` library
- `Pillow` library

## Installation

1. Clone the repository or download the script files.
2. Navigate to the directory containing the script.
3. Install the required Python packages using `requirements.txt`:

    ```
    pip3 install -r requirements.txt
    ```

## Usage

1. Place your PDF files in the `/input` folder.
2. Set the desired DPI by changing the `dpi` variable in the script.
3. Run the script:

    ```
    python3 compress_pdfs.py
    ```
