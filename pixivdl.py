from pixivpy3 import *
import json

api = AppPixivAPI()

json_result = api.user_bookmarks_illust(3983459)

#data =(json.dumps(json_result, sort_keys=True, indent=4, separators=(',', ': ')))

for x in range len(json_result.illusts):
	api.download(json_result.illusts[x].image_urls.large, "./pics/")




#file = open("userdata.txt","w")
#file.write(data)
#file.close()


