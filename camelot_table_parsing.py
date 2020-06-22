# https://camelot-py.readthedocs.io/en/master/user/quickstart.html#read-the-pdf

import camelot
import matplotlib.pyplot as plt
from pdf2image import convert_from_path

def camelot_pdf_parsing():
    pdf_configs = [{"path": "data/background_lines.pdf", "kwargs": {"process_background": True}},
                   {"path": "data/PhDThesis.pdf", "kwargs": {}}]

    for pdf_config in pdf_configs:
        print("\n#=== Parsing {} =# \n".format(pdf_config["path"]))
        tables = camelot.read_pdf(pdf_config["path"], **pdf_config["kwargs"])  # , pages="1"
        print(tables)

        for ii, table in enumerate(tables):
            table.to_csv(pdf_config["path"].replace(".pdf", f"_{ii}.csv"))
            print(table.df)

            camelot.plot(table, kind='text')
            camelot.plot(table, kind='grid')
            plt.show()


def convert_pdf_to_png(pdf_file):
    pages = convert_from_path(pdf_file, dpi=90)
    for ii, page in enumerate(pages):
        if ii > 50:
            continue
        print(f"saving page {ii}: {page}", )
        page.save(f'data/pages/out_{ii}.png', 'PNG')


def match_pdf_miner_text_to_completions_json(pdf_file):

    get_text(pdf_file)
    for page in pages():
        boxes = get_completions_json_boxes()
        text = get_text(filename)

        for text_block in text:

            if text_within_box():

                labels.append( {"text": text_block, "label": label})


def get_completions_json_boxes():
    return

def get_text(filename):
    # https://stackoverflow.com/questions/25248140/how-does-one-obtain-the-location-of-text-in-a-pdf-with-pdfminer
    from pdfminer.pdfdocument import PDFDocument
    from pdfminer.pdfpage import PDFPage
    from pdfminer.pdfparser import PDFParser
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.converter import PDFPageAggregator
    from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure

    def parse_layout(layout):
        """Function to recursively parse the layout tree."""
        for lt_obj in layout:
            print(lt_obj.__class__.__name__)
            print(lt_obj.bbox)
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                print(lt_obj.get_text())
            elif isinstance(lt_obj, LTFigure):
                parse_layout(lt_obj)  # Recursive

    fp = open(filename, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)

    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
        layout = device.get_result()
        parsed = parse_layout(layout)
        print(page, parsed)

def text_within_box():
    return

if __name__ == "__main__":
    pdf_file = "data//PhDThesis.pdf"
    #convert_pdf_to_png(pdf_file)
    match_pdf_miner_text_to_completions_json(pdf_file)
    #camelot_pdf_parsing()

