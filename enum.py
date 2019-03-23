from enum import Enum

# NOTE: Order iterating through ENUM: https://stackoverflow.com/questions/25982212/iterate-python-enum-in-definition-order
class Process(Enum):
    __order__ = "VSCODE SYS"
    SYS = {"Name": "sys", "pid":"88", "User":"system"}
    VSCODE = {"Name": "VS Code", "pid":"115", "User":"user"}

for i in Process:
    print(i) # VSCODE, SYS