from dotenv import load_dotenv
from app.utils.gui import Gui
from app.core.gemini_config import check_gemini_client
load_dotenv()

def main():

    check_gemini_client()
    Gui.MainGUI()



if __name__ == "__main__":
    main()