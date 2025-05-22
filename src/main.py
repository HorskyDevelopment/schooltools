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

commandList.append(("help", helpC, "Prints info about commands"))
     

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
    while True:
            main()
    