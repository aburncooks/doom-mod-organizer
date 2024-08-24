"""
A CLI inteface, for real DOOMers
"""
import argparse

from service.config import Config
from service.models import Launcher, Profile


if __name__ == "__main__":
    """       
    usage: dmo_cli.py [-h] -p PROFILE [-c [CONFIG]] [-e [EXEC]]

    Launch Doom Mod Organizer via CLI

    options:
    -h, --help                      show this help message and exit
    -p PROFILE, --profile PROFILE   A profile to launch DOOM with
    -c [CONFIG], --config [CONFIG]  Override config.yaml with another, better yaml file
    -e [EXEC], --exec [EXEC]        Override the profile source port with a different one
    """
    argp = argparse.ArgumentParser(prog="dmo_cli.py",
                                   description="Launch Doom Mod Organizer via CLI")
    argp.add_argument("-p", "--profile",
                      help="A profile to launch DOOM with",
                      type=str,
                      required=True)
    argp.add_argument("-c", "--config",
                      help="Override config.yaml with another, better yaml file",
                      type=str,
                      nargs="?")
    argp.add_argument("-e", "--exec",
                      help="Override the profile source port with a different one",
                      type=str,
                      nargs="?")
    args = argp.parse_args()

    if not args.config:
        args.config = "config.yaml"

    dmo_config = Config()
    dmo_config.from_yaml(args.config)

    profile = Profile()
    if args.profile:
        profile.load_profile_from_file(args.profile)

    launcher = Launcher(dmo_config)
    launcher.launch(profile)
