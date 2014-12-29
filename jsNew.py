import os
import sys


from subprocess import call


def makeDirectory(directory_name):
    if not os.path.exists(directory_name):
        print "Made directory.."
        os.makedirs(directory_name)
    else:
        print >> sys.stderr, "ERROR: Directory already exists"
        sys.exit(0)


def run(directory_name):
    dir_path = "%s/%s/" % ( os.getcwd(),  directory_name)
    print "DIR to make %s"  % dir_path
    makeDirectory(dir_path)

    # CD into our new directory
    print "Chaning into directory"
    os.chdir(dir_path)


    # Clone our sample app, which is this scrip itself =-)
    git_clone = "git clone git@github.com:jasoncbautista/jsNew.git"
    print git_clone
    os.system(git_clone)

    # Now we copy our templtes folder
    os.system("cp -rf jsNew/template/* .")
    os.system("rm jsNew")




def main():
    # Run shit here
    if len(sys.argv) <=1:
        print "Please provide a name for a repo"
        sys.exit(0)
    run(sys.argv[1])


if __name__ == "__main__":
    main()


