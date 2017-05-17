from pixivpy3 import *
from pathlib import Path
import json, os, sys

api = AppPixivAPI()

userid = input("What is your pixiv ID?: ") #put nothing in to use your last saved stuff

lastid = -1 #ideally there isn't an acutal image with id -1...

if userid=="":
	if not Path("last.txt").is_file():
		print("You've got nothing saved.")
		sys.exit()
		
	with open("last.txt") as f:
		lines = f.readlines()
		
	if len(lines)!=2:
		print("Your last.txt file is improperly formatted. Please use: userid\nimageid")
		sys.exit()
		
	userid = int(lines[0].rstrip("\n"))
	lastid = int(lines[1].rstrip("\n"))
	
else:
	userid = int(userid)

json_result = api.user_bookmarks_illust(userid) 

#data =(json.dumps(json_result, sort_keys=True, indent=4, separators=(',', ': '))) code for formatting json

folder = input("Where do you want to save your pictures?:")

os.makedirs(folder, exist_ok=True)

target = open("last.txt", 'w+')
target.write(str(userid)+"\n"+str(json_result.illusts[0].id))
target.close()

#program crashes when it's done, this is intentional
while json_result is not None:
	for x in range(len(json_result.illusts)):
	
		if(json_result.illusts[x].id == lastid):
			json_result=None
			break
		
		if(len(json_result.illusts[x].meta_pages)==0):
			api.download(json_result.illusts[x].meta_single_page.original_image_url, folder+"/")
		else:
			for image_urls in json_result.illusts[x].meta_pages:
				api.download(image_urls.image_urls.original, folder+"/")
			
	
	next_qs = api.parse_qs(json_result.next_url)
	json_result = api.user_bookmarks_illust(**next_qs)


 