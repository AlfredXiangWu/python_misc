import os
import sys
import urllib2
import socks
import socket
import httplib
import multiprocessing
from sockshandler import SocksiPyHandler


def download_image(url, save_name, proxy = False):
	try:
		fp = ''
		if proxy is True:
			opener = urllib2.build_opener(SocksiPyHandler(socks.SOCKS5, "127.0.0.1", 9999))
			fp = opener.open(url,timeout=40)
		else:
			fp = urllib2.urlopen(url, timeout=40)

		data = fp.read()
		fp.close()

		print url + ' downloading...'
		fid = open(save_name, 'w+b')
		fid.write(data)
		flag = True

		flsize = os.path.getsize(save_name)
		print 'file size:%d ' % flsize
		if flsize < 10:
			flag = False
		######
	except Exception:
		print url + ' downloading io error...       ' ,sys.exc_info()[0]
		flag = False
	return flag



def readList((list_path, save_path, log_path)):
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

		# skip the existing images
		if os.path.exists(filename):
			print filename + ' is already downloaded..'
			line = fid.readline()
			continue

		flag = download_image(url, filename, False)

		retrytimes = 1
		while flag is False:
			flag = download_image(url, filename,True)
			print 'retry times:%d' % retrytimes
			retrytimes = retrytimes + 1
			if retrytimes > 5:
				break
			
		if not flag:
			print filename + ' failed\n'
			fid_log.write(line)
			#raw_input();
		line = fid.readline()

	fid.close();
	fid_log.close();


def readPath(list_dir, save_dir, log_dir):
	count = 0;
	tasks = []
	for root, dirs, files in os.walk(list_dir):
		for fn in files:
			folder = fn.replace('.txt', '')
			log_path = log_dir + folder + '_error.txt';
			save_path = save_dir + folder + '/'
			
			tasks.append((root + fn, save_path, log_path))
			#readList((root + fn, save_path, log_path))
	pool_size = multiprocessing.cpu_count()
	pool = multiprocessing.Pool(processes=pool_size, maxtasksperchild=2)
	pool.map(readList, tasks)
	pool.close()
	pool.join()
	



if __name__ == "__main__":
	readPath("/home/xiang.wu/project/code/python/files/", "/home/xiang.wu/data/vgg_face/image/", "/home/xiang.wu/data/vgg_face/log/")