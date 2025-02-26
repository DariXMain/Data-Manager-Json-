
import main

main.excute(prg="maketb", tabelname="test_1") # Make a File

main.excute(prg="insert", tabelname="test_1", dataname="date", data="2/26/2025") # For add a data

dic = {
    "name" : "DariX",
    "age" : "15",
    "city" : "isfahan",
    "items" : [1, 2, 3],
    "details" : {
        "height" : "185",
        "weight" : "70"
    }
}

main.excute(prg="insert", tabelname="test_1", dataname="User_1", data=dic) # for add a dic


# main.excute(prg="update", tabelname="test_1", dataname="User_1", data="?") # For update a data

# main.excute(prg="remove", tabelname="test_1", dataname="User_1") # For Delete a data

