base_smaall = "https://ourartnet.com/%E5%9B%9B%E5%BA%AB%E5%85%A8%E6%9B%B8_%E7%B6%93%E9%83%A8_%E5%B0%8F%E5%AD%B8%E9%A1%9E/085_%E5%AD%AB%E6%B0%8F%E5%94%90%E9%9F%BB%E8%80%83/images/00"
base_medium = "https://ourartnet.com/%E5%9B%9B%E5%BA%AB%E5%85%A8%E6%9B%B8_%E7%B6%93%E9%83%A8_%E5%B0%8F%E5%AD%B8%E9%A1%9E/085_%E5%AD%AB%E6%B0%8F%E5%94%90%E9%9F%BB%E8%80%83/images/0"
base_large= "https://ourartnet.com/%E5%9B%9B%E5%BA%AB%E5%85%A8%E6%9B%B8_%E7%B6%93%E9%83%A8_%E5%B0%8F%E5%AD%B8%E9%A1%9E/085_%E5%AD%AB%E6%B0%8F%E5%94%90%E9%9F%BB%E8%80%83/images/"
n = []
for i in range(1,286):
	if i <= 10:
		n.append(base_smaall + str(i) + "_jpg.jpg")
	elif 10 < i < 100:
		n.append(base_medium + str(i) + "_jpg.jpg")
	else:
		n.append(base_large + str(i) + "_jpg.jpg")

n[9] = "https://ourartnet.com/%E5%9B%9B%E5%BA%AB%E5%85%A8%E6%9B%B8_%E7%B6%93%E9%83%A8_%E5%B0%8F%E5%AD%B8%E9%A1%9E/085_%E5%AD%AB%E6%B0%8F%E5%94%90%E9%9F%BB%E8%80%83/images/010_jpg.jpg"
print(n[0::])