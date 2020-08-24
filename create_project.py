import sys, os
import argparse

parser = argparse.ArgumentParser('arguments')
parser.add_argument('-name')
parser.add_argument('-path')
parser.add_argument('-type')

args = parser.parse_args()
print(args)

tmp_path = sys.argv[0].replace('/', '\\')
split_tmp_path = tmp_path.split('\\')
split_tmp_path.reverse()
PATH = tmp_path[:tmp_path.find(split_tmp_path[0])]
print(PATH)


def main():
    type_project = ''
    name = ''
    path = ''
    d_path = """D:/Projects/PycharmProjects"""
    # d_path = """C:/Projects/"""

    params = {}
    params['-p'] = d_path
    if args.name:
        name = args.name

    if args.path:
        path = args.path
    else:
        path = d_path

    if args.type:
        type_project = args.type

    tree_project(path, type_project, name)


def tree_project(path, type_, name):
    file_routes = ["/entry.py",
                   "/credentials.py",
                   "/utils.py",
                   "/logger.py",
                   "/logger.conf",
                   "/network.py",
                   "/requirements.txt",
                   "/app/__init__.py",
                   "/app/app.py",
                   "/app/routes.py",
                   "/app/api/__init__.py",
                   "/app/api/http/__init__.py",
                   "/app/api/websocket/__init__.py",
                   "/app/api/http/get_api/__init__.py",
                   "/app/api/http/post_api/__init__.py",
                   "/app/api/http/get_api/test_get.py",
                   "/app/api/http/post_api/test_post.py",
                   "/app/api/http/http_response.py",
                   "/app/api/websocket/websocket_response.py",
                   "/app/sql/sql_handler.py",
                   "/app/sql/sql_queries.py"]
    if type_ != '':
        if type_ == 'aiohttp':
            root = f"{path}/{name}"
            os.mkdir(root)  # create root project
            with open("aiohttp_template.txt", "r", encoding='utf-8-sig') as file:
                re = file.read()
                for route in file_routes:
                    if len(route.split("/")) <= 2:
                        pass
                    else:
                        route_parts = route[1:route.rfind("/")]
                        parts = route_parts.split("/")
                        tmp = ""
                        for part in parts:
                            if len(parts) <= 1:
                                tmp = f"/{part}"
                            else:
                                tmp += f"/{part}"
                        if os.path.exists(f"{root}{tmp}"):
                            pass
                        else:
                            try:
                                os.mkdir(f"{root}{tmp}")
                            except Exception as e:
                                print(e)
                    writteble_file = open(root+route, 'w', encoding="utf-8-sig")
                    writteble_file.write(re[re.find(f"[{route}]")+len(f"[{route}]")+1:re.rfind(f"[{route}]")])
                    writteble_file.close()
        else:
            print('incorrect key')


if __name__ == "__main__":
    main()
