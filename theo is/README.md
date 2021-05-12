# Theo Is
Discord Rich Presence thing that displays cycling things
#
## Instructions

1. [Get](https://www.python.org/downloads/) Python
2. Get [PyPresence](https://pypi.org/project/pypresence/)
```
pip install pypresence
```
3. [Clone](https://github.com/git-guides/git-clone) this repo
4. Edit json files to set what you want to display:

    - `config.json` is the principal file
    - `imagesList.json` is the list of images, I recommend not changing this unless you change the discord app
    - `linkList.json` is the list of links the button will take you to
    - `phrasesList.json` is the list of things the big image will display
    - `statusLink.json` is the list of things the small text will display
5. Run `main.py`:
    ```
    python3 main.py 
    ```