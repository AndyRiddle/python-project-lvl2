def determine_type_of_file(path):
    index = path.rfind('.') + 1
    return path[index:]
