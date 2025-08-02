import os
import shutil
from pathlib import Path


def remove_examples():
    example_api_path = Path(os.getcwd(), "src", "web", "api", "example")
    example_command_path = Path(os.getcwd(), "src", "commands", "example_command.py")
    for path in [example_api_path, example_command_path]:
        if path.is_dir():
            shutil.rmtree(path)
        else:
            os.remove(path)


def main():
    if "{{cookiecutter.include_examples}}".lower() == "n":
        remove_examples()


if __name__ == "__main__":
    main()
