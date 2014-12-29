import os
import sys


def makeDirectory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    else:
        print "Directory already exists"


def run(directory_name):
    dir_path = "%s/%s/" % ( os.getcwd(),  directory_name)
    print "DIR to make %s"  % dir_path
    makeDirectory(dir_path)


def main():
    # Run shit here
    if len(sys.argv) <=1:
        print "Please provide a name for a repo"
        sys.exit(0)
    run(sys.argv[1])


if __name__ == "__main__":
    main()


