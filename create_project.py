import sys, os, templates

def main():
    type_project = ''
    name = ''
    path = ''
    d_path = """D:/Projects/PycharmProjects"""
    # d_path = """C:/Projects/"""

    params = {}
    key = ''
    params['-p'] = d_path
    for i in sys.argv:
        if (i == '-n') or (i == '-p') or (i == '-t'):
            key = i
            continue
        else:
            if key != '':
                if key=='-n':
                    name = i
                elif key=='-p':
                    path = i
                elif key == '-t':
                    type_project = i
    if path == '':
        path = d_path

    tree_project(path, type_project, name)

def tree_project(path, type, name):
    slash = '/'
    #path to dirs
    root_prj = path+slash+name
    app = root_prj+slash+'app'
    views = app+slash+'views'
    #creates
    if type != '':
        if type == 'aiohttp':
            try:
                os.mkdir(root_prj)

                file = open(root_prj+slash+'entry.py', 'w')
                file.write(templates.entry)
                file.close()

                file = open(root_prj+slash+'credentials.py', 'w')
                file.write(templates.credentials)
                file.close()

                file = open(root_prj + slash + 'utils.py', 'w')
                file.write(templates.utils)
                file.close()

                file = open(root_prj+slash+'requirements.txt', 'w')
                file.write(templates.utils)
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

                file = open(views + slash + '__init__.py', 'w')
                file.write(templates.views_init)
                file.close()

                file = open(views + slash + 'response.py', 'w')
                file.write(templates.response)
                file.close()

            except OSError:
                print(OSError.errno)
            finally:
                print('Views dir is created')
        else:
            print('incorrect key')

if __name__ == "__main__":
    main()