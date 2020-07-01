import sys, os, templates
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


def tree_project(path, type, name):
    slash = '/'
    # path to dirs
    root_prj = path + slash + name
    app = root_prj + slash + 'app'
    views = app + slash + 'views'
    sql = app + slash + 'sql'
    http = views + slash + 'http'
    get_api = http + slash + 'get_api'
    post_api = http + slash + 'post_api'
    websocket = views + slash + 'websocket'
    # creates
    if type != '':
        if type == 'aiohttp':
            try:
                os.mkdir(root_prj)

                file = open(root_prj + slash + 'entry.py', 'w')
                file.write(templates.entry)
                file.close()

                file = open(root_prj + slash + 'credentials.py', 'w')
                file.write(templates.credentials)
                file.close()

                file = open(root_prj + slash + 'utils.py', 'w')
                file.write(templates.utils)
                file.close()

                file = open(root_prj + slash + 'requirements.txt', 'w')
                file.write(templates.requirements)
                file.close()
            except OSError:
                print(OSError.errno)
            finally:
                print('Project root is created')

            try:
                os.mkdir(app)

                file = open(app + slash + '__init__.py', 'w')
                file.write(templates.app_init)
                file.close()

                file = open(app + slash + 'app.py', 'w')
                file.write(templates.app)
                file.close()

                file = open(app + slash + 'routes.py', 'w')
                file.write(templates.routes)
                file.close()
            except OSError:
                print(OSError.errno)
            finally:
                print('App dir is created')

            try:
                os.mkdir(views)
                os.mkdir(http)
                os.mkdir(websocket)
                os.mkdir(get_api)
                os.mkdir(post_api)

                file = open(views + slash + '__init__.py', 'w')
                file.write(templates.views_init)
                file.close()

                file = open(http + slash + '__init__.py', 'w')
                file.write(templates.http_init)
                file.close()

                file = open(get_api + slash + '__init__.py', 'w')
                file.write(templates.get_api_init)
                file.close()
                file = open(get_api + slash + 'test_get.py', 'w')
                file.write(templates.test_get)
                file.close()

                file = open(post_api + slash + '__init__.py', 'w')
                file.write(templates.post_api_init)
                file.close()
                file = open(post_api + slash + 'test_post.py', 'w')
                file.write(templates.test_post)
                file.close()

                file = open(websocket + slash + '__init__.py', 'w')
                file.write(templates.websocket_init)
                file.close()

                file = open(http + slash + 'http_response.py', 'w')
                file.write(templates.http_response)
                file.close()

                file = open(websocket + slash + 'ws_response.py', 'w')
                file.write(templates.ws_response)
                file.close()

            except OSError:
                print(OSError.errno)
            finally:
                print('Views dir is created')

            try:
                os.mkdir(sql)

                file = open(sql + slash + 'sql_handler.py', 'w')
                file.write(templates.sql_handler)
                file.close()

                file = open(sql + slash + 'sql_queries.py', 'w')
                file.close()

            except OSError:
                print(OSError.errno)
            finally:
                print('SQL dir is created')
        else:
            print('incorrect key')


if __name__ == "__main__":
    main()
