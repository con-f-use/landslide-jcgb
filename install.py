#!/usr/bin/python
import os, sys, shutil, pkg_resources

THEMENAME = 'jcgb'


def landslide_themesdir():
    try:
        import landslide

        lsdir = os.path.abspath(os.path.dirname(landslide.__file__))
        themesdir = os.path.join(lsdir, 'themes')
        if os.path.isdir(themesdir):
            return themesdir
    except:
        return None


def main(args):
    tdir = args[0] if args else landslide_themesdir()

    if tdir is None:
        sys.stderr.write(
            "Error: Could not determine location of landslide for '{}'!\n\n"
            "Python {}\n\n"
            "Try:\n"
            "\n    * Specifying it as argument to this command\n".format(
                sys.executable, sys.version
            )
        )
        if 'landslide' not in [d.project_name for d in pkg_resources.working_set]:
            sys.stderr.write("\n    * pip install --user landslide\n")
        return 1

    if not os.path.isdir(THEMENAME):
        sys.stderr.write(
            "Error: No theme '{}' in '{}'!\n".format(THEMENAME, os.getcwd())
        )
        return 1

    shutil.copytree('jcgb', os.path.join(tdir, 'jcgb'))
    print('Copied theme to:' + tdir)
    return 0


if __name__ == '__main__':
    exit(main(sys.argv[1:]))
