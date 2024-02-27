def parse_path(abs_path: str) -> tuple:
    *path_list, file_name_with_extension = abs_path.split("/")
    name, extension = file_name_with_extension.split(".")
    return "/".join(path_list), name, extension


absolute_path = "/home/malgepav/Documents/testdir/textfile.txt"
path_elements = parse_path(absolute_path)
print(f"Path:\n"
      f"{path_elements[0]}\n"
      f"File name:\n"
      f"{path_elements[1]}\n"
      f"File extension:\n"
      f"{path_elements[2]}")
