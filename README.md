# convertAPI-python

This repository is used to convert files to desired formats that you are comfortable with. It depends on [CONVERTAPI](https://www.convertapi.com) REST-API.
<br><br>
Click here for more details on supported conversions: https://www.convertapi.com/conversions

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

### Prerequisite:
* python 3.7 or later
* convertapi

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

### Steps
1. Clone the repository:
``` 
git clone https://github.com/buster-bayliss/convertAPI-python.git
```
2. Install convertapi 
```
pip3 install --upgrade convertapi 
```
3. Sign up convertapi and get your `API-SECRET`
4. Place files to be converted in `files-to-convert` location
5. run `python3 convert.py [extension-1] [extension-2]` with two parameters for source and destination formats/extensions.
```
Example: python3 convert.py docx pdf
```
6. After execution, converted files would be available in `./converted-files` folder

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

### File Structure:

```md
.
├── converted-files
│   ├── converted-file-1.extension
│   └── converted-file-2.extension
│   └── converted-file-3.extension
│   
├── files-to-convert
│   ├── original-file-1.extension
│   └── original-file-2.extension
│   └── original-file-3.extension
│ 
├── convert.py
└── README.md
```

Please feel free to contribute / re-use.
