import shutil

path = r'./Python_Core/06/'
file_name = r'6_13.bin'
employee_residence = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}


def create_backup(path, file_name, employee_residence):
    full_path = path + '/' + file_name
    with open(full_path, 'wb') as file:
        for key, value in employee_residence.items():
            string = f'{key} {value}\n'.encode()
            print(string)
            file.write(string)

    shutil.make_archive('backup_folder', 'zip', path)

    return path + '/' + 'backup_folder.zip'

create_backup(path, file_name, employee_residence)
    