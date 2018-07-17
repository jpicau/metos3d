import os
import sys

if __name__ == "__main__":
    if len(sys.argv[:]) < 2:
        print("usage: python {0} [version]".format(sys.argv[0]))
        print("example:")
        print("$> python {0} 1.0.0".format(sys.argv[0]))
        print("current:")
        cmd = "git tag"
        print("$> " + cmd)
        os.system(cmd)
        sys.exit(0)

    version = sys.argv[1]
    print("Preparing version ....... " + version)

    filepath_in = "metos3d/__init__.template.py"
    filepath_out = "metos3d/__init__.py"

    f_in = open(filepath_in, "r", encoding="utf-8")
    f_out = open(filepath_out, "w", encoding="utf-8")

    print("Reading from ............ " + filepath_in)
    print("Writing to .............. " + filepath_out)

    f_out.write(f_in.read().format(version=version))

    f_in.close()
    f_out.close()

    cmd = "git ci -am '{0}'".format(version)
    print("Commiting ............... " + cmd)
    os.system(cmd)

    cmd = "git tag -a -m '{0}' {0}".format(version)
    print("Tagging ................. " + cmd)
    os.system(cmd)

    cmd = "git push --follow-tags"
    print("Pushing ................. " + cmd)
    os.system(cmd)

    cmd = "python setup.py sdist"
    print("Creating distribution ... " + cmd)
    os.system(cmd)

    cmd = "twine upload dist/*"
    print("Uploading to PyPI ....... " + cmd)
    os.system(cmd)


