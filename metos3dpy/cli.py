
import metos3d as m3d

def dispatch_command(args):
    if args.command == "update":
        m3d.update_metos3d()
    else:
        print("Cannot dispatch yet ... " + args.command)
