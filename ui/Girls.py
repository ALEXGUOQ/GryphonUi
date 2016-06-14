#coding:utf-8
import json

from django.http import HttpResponse
from django.shortcuts import render
from ui.DBManager import getImages,getMoreGrils
from config import pageSize,createPages

def createJson(result):
	result = json.dumps(result, sort_keys=True)
	return result

# 美女
def girls(request,pageIndex):
	pageIndex = int(request.GET.get("page", 1))
	girls = getImages(pageIndex, pageSize)
	return render(request,'girls.html',{'girls':girls})

def getMoregirls(request):
	imgs = getMoreGrils()
	imgs = json.loads(imgs)
	return HttpResponse(createJson(imgs))