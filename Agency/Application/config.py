from pathlib import Path

APPLICATION_DIR = Path.cwd()
ROOT_DIR = APPLICATION_DIR.parent
RESOURCES_DIR = ROOT_DIR.joinpath("Resources")

ICON = RESOURCES_DIR.joinpath("icon.png")
STYLE = RESOURCES_DIR.joinpath("style.qss")

BUTTONS = RESOURCES_DIR.joinpath("Buttons")
BUTTON_LOGIN = BUTTONS.joinpath("prijava.jpg")
BUTTON_REGISTER = BUTTONS.joinpath("registracija.jpg")

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

LOGIN_UI_PATH = VIEW_DIR.joinpath("loginView.ui")
REGISTER_UI_PATH = VIEW_DIR.joinpath("registerView.ui")
ADMIN_UI_PATH = VIEW_DIR.joinpath("adminView.ui")
OWNER_UI_PATH = VIEW_DIR.joinpath("ownerView.ui")
AGENT_UI_PATH = VIEW_DIR.joinpath("agentView.ui")
USER_UI_PATH = VIEW_DIR.joinpath("userView.ui")
PROPERTY_UI_PATH = VIEW_DIR.joinpath("propertyView.ui")
VISITS_UI_PATH = VIEW_DIR.joinpath("visitsView.ui")

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
