# convertAPI-python

This repository is used to convert files to desired formats that you are comfortable with. It depends on [CONVERTAPI](https://www.convertapi.com) REST-API. 

### Prerequisite:
* python 3.7 or later
* convertapi

### Steps
1. Clone https://github.com/buster-bayliss/convertAPI-python.git
2. Install convertapi 
```
pip3 install --upgrade convertapi 
```
3. Sign up convertapi and get your `API-SECRET`
4. Place files to be converted in `files-to-convert` location
4. run `python3 convert.py [extension-1] [extension-2]` with two parameters for source and destination formats/extensions.
5. After execution, converted files would be available in `./converted-files` folder

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

