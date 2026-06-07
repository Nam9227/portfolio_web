import fitz
import os

pdf_files = [
    "Bài tập 1.pdf",
    "Baitap2.pdf",
    "Bai 3.pdf",
    "Tuan 4.pdf",
    "Bài 5.pdf",
    "tmpmox2oh_tuan6-2.pdf",
    "tuan 7.pdf"
]

input_dir = r"d:\CS_AI"
output_dir = r"d:\CS_AI\portfolio_web\images"

os.makedirs(output_dir, exist_ok=True)

for i, pdf_name in enumerate(pdf_files):
    pdf_path = os.path.join(input_dir, pdf_name)
    if not os.path.exists(pdf_path):
        print(f"Skipping PDF {i} because it doesn't exist.")
        continue
    
    doc = fitz.open(pdf_path)
    print(f"Extracting images from PDF {i}")
    for page_index in range(len(doc)):
        page = doc[page_index]
        image_list = page.get_images(full=True)
        if image_list:
            print(f"[+] Found {len(image_list)} images in page {page_index}")
        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # Use safe ASCII names
            image_filename = f"proj{i+1}_p{page_index}_{image_index}.{image_ext}"
            image_path = os.path.join(output_dir, image_filename)
            
            with open(image_path, "wb") as f:
                f.write(image_bytes)
            print(f"Saved {image_filename}")
