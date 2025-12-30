from CreaterFolders import CreaterFolders

def main():
    msg = input("Enter password: ")

    if msg == "2710":
        CreaterFolders()
    else:
        print("Incorrect password.")

if __name__ == "__main__":
    main()
