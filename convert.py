import convertapi
import glob, sys

# initial assignation
count = 1
sourceFormat = sys.argv[1]
destinationFormat = sys.argv[2]
convertapi.api_secret = 'YOUR-API-SECRET'

# get source files to be converted
getSourceLocation = "./files-to-convert/*."+sourceFormat
sourceFilesPaths = glob.glob(getSourceLocation)

# destination folder path
getDestinationLocation = "./converted-files/"

if(sourceFilesPaths):

	# loop through all the files
	for filePath in sourceFilesPaths:

		print("converting file "+str(count)+"..")

		convertapi.convert(destinationFormat, {
		    'File': filePath
		}, from_format = sourceFormat).save_files(getDestinationLocation)

		count = count + 1
else:
	print("There is No such files available.\nPlease Check the format properly.")
	print("See supported conversions on https://www.convertapi.com/conversions")

