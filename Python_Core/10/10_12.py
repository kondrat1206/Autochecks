class IDException(Exception):
    print("Exception")


def add_id(id_list, employee_id):
    if str(employee_id).startswith("01"):
        id_list.append(employee_id)
        print(id_list)
        return id_list
    else:
        raise IDException()
    

add_id([], 113)