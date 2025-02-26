# writed by DariX:(Ariyan) --- 2/24/2025

import os, sys
import json


Folder_name = "json_datas"
os.makedirs(Folder_name, exist_ok=True)

class Hand_query:

    def check_accept_value(value):
        if not type(value) in [str, int, bytes, dict, list, set, float, bool, tuple]:
            return False
        
        return True

    def make_tabel(tabel_name : str):
        if os.path.exists(Folder_name + f"/{tabel_name}.json"):
            return "Error : Tabel with name exist !"
        else:
            with open(Folder_name + f"/{tabel_name}.json", "w") as file:
                secend_tabel = {
                    "tabel_name" : str(tabel_name)
                }
                file.write(json.dumps(secend_tabel))
                file.close()

    def make_data(tabel_name, data_name, data):
        if Hand_query.check_accept_value(tabel_name) and Hand_query.check_accept_value(data_name) and Hand_query.check_accept_value(data):
            try:
                with open(Folder_name + f"/{tabel_name}.json") as read_file_1:
                    json_file_1 = json.load(read_file_1)

                json_file_2 = {
                    data_name : data
                }

                json_file_3 = {**json_file_1, **json_file_2}

                with open(Folder_name + f"/{tabel_name}.json", "w") as file:
                    file.write(json.dumps(json_file_3))
                    file.close()
            except FileNotFoundError:
                return "Tabel Name Wrang"
            
    def get_data(tabel_name, data_name):
        if Hand_query.check_accept_value(tabel_name) and Hand_query.check_accept_value(data_name):
            try:
                with open(Folder_name + f"/{tabel_name}.json") as read_file_1:
                    json_file_1 = json.load(read_file_1)

                return json_file_1[data_name]

            except FileNotFoundError:
                return "Tabel Name Wrang"
            
    def get_all_data(tabel_name):
        if Hand_query.check_accept_value(tabel_name):
            try:
                with open(Folder_name + f"/{tabel_name}.json") as read_file_1:
                    json_file_1 = json.load(read_file_1)

                return json_file_1

            except FileNotFoundError:
                return "Tabel Name Wrang"
            
    def uppdate_data(tabel_name, data_name, new_data):
        if Hand_query.check_accept_value(tabel_name) and Hand_query.check_accept_value(data_name) and Hand_query.check_accept_value(new_data):
            try:
                with open(Folder_name + f"/{tabel_name}.json") as read_file_1:
                    json_file_1 = json.load(read_file_1)

                json_file_1[data_name] = new_data

                with open(Folder_name + f"/{tabel_name}.json", "w") as file:
                    file.write(json.dumps(json_file_1))
                    file.close
                
            except FileNotFoundError:
                return "Tabel Name Wrang"

    def remove_data(tabel_name, data_name):
        if Hand_query.check_accept_value(tabel_name) and Hand_query.check_accept_value(data_name):
            try:
                with open(Folder_name + f"/{tabel_name}.json") as read_file_1:
                    json_file_1 = json.load(read_file_1)

                del json_file_1[data_name]

                with open(Folder_name + f"/{tabel_name}.json", "w") as file:
                    file.write(json.dumps(json_file_1))
                    file.close
                
            except FileNotFoundError:
                return "Tabel Name Wrang !"
    

print(Hand_query.remove_data("DariX", "car"))