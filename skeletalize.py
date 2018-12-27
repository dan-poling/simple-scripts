
def skeletize(file_in, file_out):
    import pandas as pd
    import re

    # read in the data and check it
    df = pd.read_excel(file_in, index_col=0)

    # use these regex objects to remove references and suffixe placeholders
    brak_regex = re.compile(r'(\[.*\])')
    paren_regex = re.compile(r'(\([ijk]\))')

    # create a new column, there has to be a way to do this in 1 step
    df['skeletal'] = df['path'].replace(to_replace=brak_regex, value='', regex=True)
    df['skeletal'] = df['skeletal'].replace(to_replace=paren_regex, value='', regex=True)

    df.to_excel(file_out)

file_in = 'Mapping.xlsx'
file_out = 'skeletal-mapping.xlsx'
skeletize(file_in, file_out)