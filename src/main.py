import ytDownload  

commandList = [
    ("download", ytDownload.download, "Downloads a YT vid"),
]


def helpC(command = None):
    if command == None:
        print("Commands: ")
        for i in commandList:
            print(i[0]+" "+i[2])
    else:
        for i in commandList:
            if command == i[0]:
                print(i[2])
                return
            else:
                print('No such command!')   

def print_shape():
    # Store each row with preserved spacing
    rows = [
        "     /\\  \\         /\\  \\         /\\__\\         /\\  \\         /\\  \\         /\\  \\         /\\__\\     /\\  \\    ",
        "    /::\\  \\       /::\\  \\       /:/  /         \\:\\  \\       /::\\  \\       /::\\  \\       /:/  /    /::\\  \\   ",
        "   /:/\\ \\  \\     /:/\\:\\  \\     /:/__/           \\:\\  \\     /:/\\:\\  \\     /:/\\:\\  \\     /:/  /    /:/\\ \\  \\  ",
        "  _\\:\\~\\ \\  \\   /:/  \\:\\  \\   /::\\  \\ ___       /::\\  \\   /:/  \\:\\  \\   /:/  \\:\\  \\   /:/  /    _\\:\\~\\ \\  \\ ",
        " /\\ \\:\\ \\ \\__\\ /:/__/ \\:\\__\\ /:/\\:\\  /\\__\\     /:/\\:\\__\\ /:/__/ \\:\\__\\ /:/__/ \\:\\__\\ /:/__/    /\\ \\:\\ \\ \\__\\",
        " \\:\\ \\:\\ \\/__/ \\:\\  \\  \\/__/ \\/__\\:\\/\\/  /    /:/  \\/__/ \\:\\  \\ /:/  / \\:\\  \\ /:/  / \\:\\  \\    \\:\\ \\:\\ \\/__/",
        "  \\:\\ \\:\\__\\    \\:\\  \\            \\::/  /    /:/  /       \\:\\  /:/  /   \\:\\  /:/  /   \\:\\  \\    \\:\\ \\:\\__\\  ",
        "   \\:\\/:/  /     \\:\\  \\           /:/  /     \\/__/         \\:\\/:/  /     \\:\\/:/  /     \\:\\  \\    \\:\\/:/  /  ",
        "    \\::/  /       \\:\\__\\         /:/  /                     \\::/  /       \\::/  /       \\:\\__\\    \\::/  /   ",
        "     \\/__/         \\/__/         \\/__/                       \\/__/         \\/__/         \\/__/     \\/__/    "
    ]
    
    # Print each row with explicit newline
    for row in rows:
        print(row)

commandList.append(("help", helpC, "Prints info about commands"))
commandList.append(("logo", print_shape, "Prints the logo of this tool"))     

def main():

    command = input("> ")

    for i in commandList:
        if i[0] == command:
            print(i)
            i[1]()
            return
    else:
        print("No sutch command! Try help.")

if __name__ == "__main__":
    print_shape()
    try:
        while True:
                main()
    except KeyboardInterrupt:
        print("Bye!")
        quit()