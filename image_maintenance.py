import requests
import os
import sys

API_URL = ""
API_IMG_ARRAY_NAME = "image_in_use"
IMAGE_PATH_ON_SERVER = ""

def remove_unused_images():
	print "Trying to get an array with images in use..."
	response = requests.get(API_URL)
	if response.status_code != 200:
		print >> sys.stderr, "Something went wrong, cant reach the server."
	else:
		print "Images received, searching unused ones."
		img_array = response.json()[API_IMG_ARRAY_NAME]
		for curr_dir, sub_folders, files in os.walk(IMAGE_PATH_ON_SERVER):
			for img in files:
		    		if not img in img_array:
		    			try:
		    				print "\tRemoving " + img + " at " + curr_dir
		    				os.remove(curr_dir + "/" + img)
		    			except IOError, e:
		    				print >> sys.stderr, str(e)

if __name__ == "__main__":
	print "Starting image maintenance script."
	remove_unused_images()
