#-*- coding:utf-8 -*-
import random
from ui.models import Image,Photography
from django.core import serializers

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
	list = Image.objects.filter(tags__contains=tag).all()[start:end]
	return list

# 获取图片的所有张数
def getfilterImagesCount(tag):
	count = len(Image.objects.filter(tags__contains=tag).all())
	return count

# 获取照片
def getPhotos(pageIndex,pageSize):
	start = (pageIndex - 1) * pageSize
	end = start + pageSize
	list = Photography.objects.all()[start:end]
	return list

# 获取照片的所有张数
def getPhotosCount():
	count = len(Photography.objects.all())
	return count

def getMoreGrils():
	start = random.randint(1,getImagesCount())
	end = start + 20
	return serializers.serialize('json',Image.objects.all()[start:end])