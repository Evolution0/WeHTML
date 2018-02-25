import os


def start():
    print("\nWeHTML initially made by Aidan Welch\n")
    print("This is a tool for converting HTML code into code usable with Wemos.")
    input("Press Enter(Return) to continue...")
    find_file()


def find_file():
    location = input("Input your file's location: ")
    if len(location) < 1:
        print("You didn't type anything")
        find_file()
    else:
        # Opens the file and confirms if its correct
        with open(location) as file:
            print("Following will be the first 4 characters of {0}:".format(os.path.basename(location)))
            print(file.read(4))
            while True:
                answer = input("Type Y if correct or N if false: ")
                if answer.upper() == "Y":
                    get_html(location)
                    break
                elif answer.upper() == "N":
                    find_file()
                    break
                else:
                    continue


def get_html(location):
    # must reopen file because every time file is read it saves cursor position
    template = """#define USE_PROGMEM 1\nconst char* webPage PROGMEM = R"\n{1}";\n{0}.send(200, "text/html", webPage)"""
    new_file = input("Where should the new file(include the name for the file in the path) be saved: ")
    with open(location) as file, open(new_file, "w+") as output_file:
        client = input("What is the name of the variable holding your WI-FI client: ")
        output_file.write(template.format(client, file.read()))

        print("Done!")


if __name__ == '__main__':
    start()
