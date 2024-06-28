import os
import fitz  # PyMuPDF
import shutil
from PIL import Image

"""
Convert PDF pages to images at the specified DPI.
    
:param input_path: Path to the input PDF file.
:param dpi: Resolution in dots per inch.
:return: List of PIL Image objects.
"""
def pdf_to_images(input_path: str, dpi: int):
    doc = fitz.open(input_path)
    images = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(dpi=dpi)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)
    
    doc.close()
    return images

"""
Compress the PDF to the target size.

:param input_path: Path to the input PDF file.
:param output_path: Path to the output compressed PDF file.
:param target_size: Target size in bytes.
"""
def compress_pdf(input_path: str, output_path: str, dpi: int):
    input_doc = fitz.open(input_path)
    input_doc.save(output_path)
    input_doc.close()
    images = pdf_to_images(output_path, dpi)
    if images:
        images[0].save(output_path, save_all=True, append_images=images[1:])


"""
Compress all PDFs in the specified folder to the target size.

:param folder_path: Path to the folder containing PDF files.
:param target_size_mb: Target size in megabytes.
"""
def compress_pdfs_in_folder(input_folder_path: str, output_folder_path:str, dpi: int):
    target_size_bytes = target_size_mb * 1024 * 1024
    for filename in os.listdir(input_folder_path):
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(input_folder_path, filename)
            output_path = os.path.join(output_folder_path, filename)
            print(f"Compressing {filename}...")

            shutil.copy(input_path, output_path)
            compress_pdf(input_path=input_path, output_path=output_path, dpi=dpi)
            final_size = os.path.getsize(output_path)
            print(f"Compressed {filename} to {final_size / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    target_size_mb = 1  
    compress_pdfs_in_folder(
        input_folder_path="./input",
        output_folder_path = "./output",
        dpi=160, # Target DPI
    )
