# writed by DariX:(Ariyan) --- 2/24/2025

import os
import query

Options = [
    "maketb", # For Make a database *
    "insert", # For Make a data * 
    "update", # For Update data *
    "remove", # For remove data *
    "select" # For get a data *
    "selectall" # For get all data*
]

def excute(**option):
    try:
        if not option["prg"] in Options:
            return f"Error NotProgram in -{option["prg"]}-"
        
        if option["prg"] == "maketb":
            return query.Hand_query.make_tabel(option["tabelname"])
        elif option["prg"] == "insert":
            return query.Hand_query.make_data(option["tabelname"], option["dataname"], option["data"])
        elif option["prg"] == "select":
            return query.Hand_query.get_data(option["tabelname"], option["dataname"])
        elif option["prg"] == "selectall":
            return query.Hand_query.get_all_data(option["tabelname"])
        elif option["prg"] == "update":
            return query.Hand_query.uppdate_data(option["tabelname"], option["dataname"], option["data"])
        elif option["prg"] == "remove":
            return query.Hand_query.remove_data(option["tabelname"], option["dataname"])

    except KeyError:
        return "Error : Not Found A Element (prg/tabelname/dataname/data)"
    