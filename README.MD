# Decipher
DecipherV2 is a remake of my previous project. Using **customtkinter** for GUI it can decode most popular ciphers. Originally made to make solving ARG a bit easier.

Created by StalZi
## Build
You can build the program from source code yourself with **pyinstaller**:

`pip install pyinstaller`

`pyinstaller --noconfirm --windowed -D -n "DecipherV2" --add-data "locales;locales" --add-data "<YOUR_SITE-PACKAGES_FOLDER_HERE>\customtkinter;customtkinter/" --contents-directory "." main.py`

Instead of **<YOUR_SITE-PACKAGES_FOLDER_HERE>** you need to put path to your python site-packages folder. You can get it with any **pip show**, for example with customtkinter:

`pip show customtkinter`

## Install
Just go to the [releases tab](https://github.com/StalZi/DecipherV2/releases), download the latest release and launch DecipherV2 x.x.x.exe