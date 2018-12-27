'''
This expects a 2 columns sheet where the 2nd column, named "path" contains complex, or full xpaths.
'''

def skeletize(file_in, file_out):
    import pandas as pd
    import re

    df = pd.read_excel(file_in, index_col=0)

    # this finds id references e.g., "[Roles/Role='Borrower' and @id=/.../@id]"
    brak_regex = re.compile(r'(\[.*\])')
    
    # this finds suffix placeholders e.g., "(i)"
    paren_regex = re.compile(r'(\([ijk]\))')

    # create a new column and remove id references and suffix placeholders
    df['skeletal'] = df['path'].replace(to_replace=brak_regex, value='', regex=True)
    df['skeletal'] = df['skeletal'].replace(to_replace=paren_regex, value='', regex=True)

    df.to_excel(file_out)

file_in = 'filename.xlsx'
file_out = 'skeletal-mapping.xlsx'
skeletize(file_in, file_out)
