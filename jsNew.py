import os
import sys


def makeDirectory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def run(directory_name):
    dirToMake = "%s/%s/" % ( os.getcwd() ,  directory_name)
    print "DIR to make %s"  % directory_name


def main():
    # Run shit here
    if len(sys.argv) <=1:
        print "Please provide a name for a repo"
        sys.exit(0)
    run(sys.argv[1])


if __name__ == "__main__":
    main()


