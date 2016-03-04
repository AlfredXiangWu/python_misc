import os
import urllib2

def download_image(url, save_name):
	try:
		fp = urllib2.urlopen(url, timeout=60)
		data = fp.read()
		fp.close()

		print url + ' downloading...'
		fid = open(save_name, 'w+b')
		fid.write(data)
		flag = True 
	except IOError, HTTPError:
		print url + ' downloading error...'
		flag = False
	return flag

def readList(list_path, save_path, log_path):
	if not os.path.exists(save_path):
		os.mkdir(save_path)

	fid = open(list_path, 'r')
	fid_log = open(log_path, 'w')
	line = fid.readline()
	count = 1
	while line:
		tmp = line.split(' ')
		name = tmp[0]
		url = tmp[2]
		filename = save_path + name + '.jpg'
		flag = download_image(url, filename)
		if not flag:
			fid_log.write(line + '\n')
			#raw_input();
		line = fid.readline()

	fid.close();
	fid_log.close();


def readPath(list_dir, save_dir, log_dir):
	count = 0;
	for root, dirs, files in os.walk(list_dir):
		for fn in files:
			folder = fn.replace('.txt', '')
			log_path = log_dir + folder + '.txt';
			save_path = save_dir + folder + '/'
			print root + fn
			print save_path
			readList(root + fn, save_path, log_path)



if __name__ == "__main__":
	readPath("/home/xiang.wu/project/code/python/files/", "/home/xiang.wu/data/vgg_face/image/", "/home/xiang.wu/data/vgg_face/log/")