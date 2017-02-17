from openpyxl import load_workbook
import os
import json

def parse_all():
    """Returns a list of dictionaries representing the data parsed from /data directory."""
    file_names = map(lambda x: ("../data/" + x, x.split(".")[0]), os.listdir("../data"))
    workbooks = map(lambda x: (load_workbook(x[0]), x[1]),
                    file_names)
    sheets = map(lambda x: (x[0]["Sheet1"], x[1]),
                 workbooks)
    dataset = [{"id": sheet[1],
                "jump": sheet[0]["C2"].value,
                "age": sheet[0]["C4"].value,
                "exercise": sheet[0]["C5"].value,
                "competitive": sheet[0]["C6"].value,
                "height": sheet[0]["C7"].value,
                "weight": sheet[0]["C8"].value,
                "gender": sheet[0]["C9"].value,
                "injury": sheet[0]["C10"].value,
                "color": sheet[0]["C11"].value,
                "sleep": sheet[0]["C12"].value,
                "race": sheet[0]["C13"].value,}

                for sheet in sheets]
    return dataset

def parse_all_to_json(file):
    """Write the returned list from parse_all in JSON format to 'file'."""
    json.dump(parse_all(), open(file, "w"), indent=4)