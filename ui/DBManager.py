#-*- coding:utf-8 -*-
from ui.models import Image

# 获取图片
def getImages(pageIndex,pageSize):
	start = (pageIndex - 1) * pageSize
	end = start + pageSize
	list = Image.objects.all()[start:end]
	return list

# 获取图片的所有张数
def getImagesCount():
	count = len(Image.objects.all())
	return count

# 获取过滤图片
def filterImages(tag,pageIndex,pageSize):
	start = (pageIndex - 1) * pageSize
	end = start + pageSize
	list = Image.objects.filter(tags=tag).all()[start:end]
	return list

# 获取图片的所有张数
def getfilterImagesCount(tag):
	count = len(Image.objects.filter(tags=tag).all())
	return count
