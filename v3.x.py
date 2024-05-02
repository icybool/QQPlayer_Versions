import os
import requests
import colorama

urls = []
cnt = 200

# colorama.init(autoreset = True)
for i in range(30, 40):
	for j in range(cnt, 1000):
		url = f"https://dldir1.qq.com/qqyy/pc/QQPlayer_Setup_{i}_{j}.exe"
		print(colorama.Style.BRIGHT + colorama.Fore.BLUE + "[ CHECKING ]" + colorama.Style.RESET_ALL + f" {url}")
		if (requests.head(url).status_code == 200):
			print(colorama.Style.BRIGHT + colorama.Fore.GREEN + "[ RIGHTURL ]" + colorama.Style.RESET_ALL + f" {url}")
			urls.append(url)

with open('v3.x.txt', 'w') as file:
	file.write("\n".join(urls) + "\n")
