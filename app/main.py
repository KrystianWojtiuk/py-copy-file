def copy_file(command: str) -> None:
    names = command.split(" ")
    if len(names) == 3:
        if names[1] == names[2]:
            return
        if names[0] == "cp":
            try:
                with (open(names[1], "r") as file_in,
                      open(names[2], "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                print("File not found")
