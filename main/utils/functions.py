import os

import openpyxl


def xls_to_json() -> list:
    base_dir = os.path.abspath(os.getcwd())
    workbook = openpyxl.load_workbook(base_dir + '/schema.xlsx')
    worksheet = workbook.active

    names = ('chapter', 'name', 'parent_id', 'schema_id', 'rus', 'china', 'quantity', 'description')
    data = []

    for row in worksheet.iter_rows(min_row=2, min_col=1, max_row=3562, max_col=8):
        if row[3].value is None or row[2].value is None:
            continue
        column = 0
        sub_data = {}
        for cell in row:
            sub_data[names[column]] = cell.value
            column += 1
        data.append(sub_data)

    return data
