from PyPDF2 import PdfReader, PdfWriter
import os
import tqdm

def crop_pdf(input_pdf_path, output_pdf_path, crop_box):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        page.cropbox.lower_left = (crop_box['lower_left_x'], crop_box['lower_left_y'])
        page.cropbox.upper_right = (crop_box['upper_right_x'], crop_box['upper_right_y'])
        writer.add_page(page)

    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)

if __name__ == "__main__":

    crop_box = {
        'lower_left_x': 0,
        'lower_left_y': 115,
        'upper_right_x': 592,
        'upper_right_y': 640
    }

    pdf_root_dir = r'F:\胃镜报告单'
    save_dir = r'F:\胃镜报告单crop_pdf'
    for root, dirs, files in os.walk(pdf_root_dir):
        for file in tqdm.tqdm(files):
            if file.endswith('.pdf'):
                input_pdf_path = os.path.join(root, file)
                output_pdf_path = os.path.join(save_dir, file.replace('.pdf', '_crop.pdf'))
                if os.path.exists(output_pdf_path):
                    print(f"{output_pdf_path} 已存在，跳过")
                    continue
                crop_pdf(input_pdf_path, output_pdf_path, crop_box)
                print(f"裁剪 {input_pdf_path} 完成，输出文件为 {output_pdf_path}")
            
