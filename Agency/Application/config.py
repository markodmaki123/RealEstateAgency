from pathlib import Path

APPLICATION_DIR = Path.cwd()
ROOT_DIR = APPLICATION_DIR.parent

MODEL_DIR = ROOT_DIR.joinpath("Model")
VIEW_DIR = ROOT_DIR.joinpath("View")
CONTROLLER_DIR = ROOT_DIR.joinpath("Controller")
DATA_DIR = ROOT_DIR.joinpath("Data")
RESOURCES_DIR = ROOT_DIR.joinpath("Resources")
DATE_FORMAT = "%d.%m.%Y."

USERS_PATH = DATA_DIR.joinpath("users.json")
REAL_ESTATES_PATH = DATA_DIR.joinpath("real_estates.json")
VISITS_PATH = DATA_DIR.joinpath("visits.json")
AGENCIES_PATH = DATA_DIR.joinpath("agencies.json")
ADDRESSES_PATH = DATA_DIR.joinpath("addresses.json")

if __name__ == "__main__":
    print()
    print(APPLICATION_DIR)
    print(ROOT_DIR)
    print()
    print(CONTROLLER_DIR)
    print(DATA_DIR)
    print(MODEL_DIR)
    print(VIEW_DIR)
    print()
