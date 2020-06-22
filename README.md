## pdf_parsing
To le tme parse tables, text and contextual information.

### Conda installation (better use a environment.yml)
conda install -c conda-forge camelot-py


### About tabula
>> from tabula import read_pdf
>> df_list = read_pdf("example.pdf", encoding='utf-8', spreadsheet=True, pages='all', multiple_tables=True)


### Label-studio
- label-studio start ./pdf_parsing


### Procedure
> conda activate pdf_parsing
> python camelot_table_parsing.py
> label-studio init --input-path=data/pages --input-format=image-dir --label-config=label-studio-template/config.xml --allow-serving-local-files label-studio-pages/
> label-studio start ./label-studio-pages/
