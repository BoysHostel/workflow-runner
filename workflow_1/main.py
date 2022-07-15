from Service.runner import json_reader, json_printer
import os


print(os.getcwd())
json_str = json_reader(os.getcwd() + "/Service/sample.json")
json_printer(json_str)