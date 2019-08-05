#!/usr/bin/env python3.5

# super simple file renamer based on position in directory listing
# there is a fall back when an extension is not present


import os
import magic

example = {
	"home": {
		"jared":{
			"Desktop": ["file_one.png", "data.csv"],
			"Pictures": ["example.jpg"]
		}
	}
}
def get_mime(file_path: str):
	mime = magic.Magic(mime=True)
	return mime.from_file(file_path).split("/")[1]

name_dictionary = {
	"img": {
		"count": 0,
		"extensions": ["jpg", "png", "tiff"]
	},
	"document": {
		"count": 0,
		"extensions": ["docx", "pdf", "pptx"]
	},
}

directory = "random_garbage"
for fi in os.listdir(directory):
	extension = fi.split('.')[1]
	if(len(extension) == 0):
		extension = get_mime(fi)
	for key, value in name_dictionary.items():
		if(extension in value['extensions']):
			original_filename = "{}/{}".format(directory, fi)
			new_filename = "{}/{}_{}.{}".format(directory, key, value['count'], extension) 
			print("{} -----------> {}".format(original_filename, new_filename))
			os.rename(original_filename, new_filename)
			value['count']+=1
