import json

with open("euro.json", "r") as file:
    data = json.load(file)
    string = "Date        " + "Buying rate   " + "Selling rate"
    border = "===================================="
    print(string)
    print(border)
    rates = data["rates"]


    for item in rates:
       line = str(item["effectiveDate"]) + "    " + str(item["bid"]) + "      " + str(item["ask"])
       print(line)