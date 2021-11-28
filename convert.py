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

		convertapi.convert(sourceFormat, { 
			'File': filePath 
		}).file.save(getDestinationLocation+'converted-file-'+str(count)+"."+destinationFormat)

		count = count + 1