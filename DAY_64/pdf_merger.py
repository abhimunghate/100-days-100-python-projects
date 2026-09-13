import os
from PyPDF2 import PdfReader, PdfWriter

def is_blank_page(page):
    """Checks whether a PDF page is blank.

    A page is considered blank when it contains no extractable text and has no annotations."""
    try:
        text = page.extract_text() or ""
        annotations = page.get("/Annots")
        return not text.strip() and not annotations
    except Exception:
        return False

def get_page_numbers(total_pages, start_page, end_page):
    """Converts user-entered 1-based page ranges into valid page indexes.

    Example:
    Input: 2-5
    Output: [1, 2, 3, 4]
    """
    start_page = max(1, start_page)
    end_page = min(total_pages, end_page)

    if start_page > end_page:
        return []
    return list(range(start_page - 1, end_page))

def merge_selected_pdfs(pdf_files, output_file, remove_blank_pages=True):
    """Merges selected page ranges from multiple PDF files.

    pdf_files format: [{"path": "file1.pdf", "start": 1, "end": 3}, {"path": "file2.pdf", "start": 2, "end": 5}]"""
    writer = PdfWriter()
    total_added_pages = 0

    for pdf_data in pdf_files:
        pdf_path = pdf_data["path"]
        start_page = pdf_data["start"]
        end_page = pdf_data["end"]

        reader = PdfReader(pdf_path)
        page_indexes = get_page_numbers(len(reader.pages), start_page, end_page)
        for page_index in page_indexes:
            page = reader.pages[page_index]

            if remove_blank_pages and is_blank_page(page):
                continue
            writer.add_page(page)
            total_added_pages += 1

    if total_added_pages == 0:
        raise ValueError("No pages were available to merge.")

    with open(output_file, "wb") as output_pdf:
        writer.write(output_pdf)
    return total_added_pages

def get_pdf_page_count(pdf_path):
    reader = PdfReader(pdf_path)
    return len(reader.pages)

# Done