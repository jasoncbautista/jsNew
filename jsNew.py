import os


def makeDirectory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)



def main():
    # Run shit here
    print "yo"


if __name__ == "__main__":
    main()


