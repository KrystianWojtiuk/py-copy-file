def copy_file(command: str) -> None:
    if command[:2] == "cp":
        names = command.split(" ")
        if len(names) == 3:
            if names[1] == names[2]:
                return
            try:
                with (open(names[1], "r") as file_in,
                      open(names[2], "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError as e:
                print(f"File {e.filename} not found")
