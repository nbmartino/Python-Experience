import pathlib

from convert_server_name_linux import convert

HERE = pathlib.Path(__file__).parent

server_list = [x.lower().strip() for x in
                         open(HERE / "servers" / "server_names_cleaned_list.txt", 'r').readlines()]
for server in server_list:
    print(convert(server))