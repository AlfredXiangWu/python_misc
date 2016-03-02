import os


def readList(list_path, save_dir):
	if not os.
	fid = open(list_path, 'r')
	line = fid.readline()
	count = 1
	while line:
		tmp = line.split(' ')
		name = tmp[0]
		url = tmp[2]


def readPath(list_dir, save_dir):
	count = 0;
	for root, dirs, files in os.walk(list_dir):
		for fn in files:
			folder = fn.replace('.txt', '')
			save_path = save_dir + folder
			print root + fn
			print save_path
			readList(root + fn, save_path)



if __name__ == "__main__":
	readPath("/home/xiang.wu/project/code/python/files/", "/home/xiang.wu/data/vgg_face/")