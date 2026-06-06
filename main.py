import argparse
from pathlib import Path
from operations import organize_directory

def main():
    # Creating the argument parser object
    parser = argparse.ArgumentParser(
        description="An automated file organizer utility."
    )
    
    # Tell it to expect a target path string from the user
    parser.add_argument(
        "target_path",
        type=str,
        help="The absolute or relative path to the directory you want to clean up."
    )

    # Parse the arguments typed in the terminal
    args = parser.parse_args()

    # Converting the input string to a real system Path object
    # .expanduser() handles paths like '~/' by converting them to '/home/user/'
    chosen_directory = Path(args.target_path).expanduser().resolve()

    organize_directory(chosen_directory)

if __name__ == "__main__":
    main()