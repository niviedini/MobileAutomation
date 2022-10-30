import os
import platform


def print_name(name, typ):
    print(f"{name} is {typ}")


if __name__ == '__main__':
    print(f"Ajay likes Nivi {1+1} times")
    print(os.getcwd())
    print(platform.system())
    info = [{
                "Name": "Nivi",
                "Type": "daffa",
            },
            {
                "Name": "Aadhya",
                "Type": "daffa",
            },
            {
                "Name": "Ajay",
                "Type": "Good",
            }]
    for daffa in info:
        print_name(name=daffa["Name"], typ=daffa["Type"])
