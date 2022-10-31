import os
import platform
from helpers.common import print_name


if __name__ == '__main__':
    print(f"Ajay likes Nivi {1+1} times")
    print(os.getcwd())
    print(platform.system())
    info = [{
                "Name": "Nivi",
                "Type": "jaffa",
            },
            {
                "Name": "Aadhya",
                "Type": "Good",
            },
            {
                "Name": "Ajay",
                "Type": "Good",
            }]
    for daffa in info:
        print_name(name=daffa["Name"], typ=daffa["Type"])
