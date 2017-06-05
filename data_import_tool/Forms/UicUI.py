import os


def get_ui_files(path):
    files = []
    for root, dirnames, filenames in os.walk(path):
        for file_name in filenames:
            print os.path.splitext(file_name)[1]
            if os.path.splitext(file_name)[1] == '.ui':
                file_path = os.path.join(root, file_name)
                files.append(file_path)
    return files


def pyuic5_ui_files(files):
    for ui_file in files:
        ui_basename = os.path.splitext(os.path.basename(ui_file))[0]
        print "pyuic5 -o ..\UI%s.py %s.ui" % (ui_basename, ui_basename)
        os.system("pyuic5 -o ..\UI%s.py %s.ui" % (ui_basename, ui_basename))


if __name__ == '__main__':
    ui_path = os.getcwd()
    ui_files = get_ui_files(ui_path)
    pyuic5_ui_files(ui_files)
