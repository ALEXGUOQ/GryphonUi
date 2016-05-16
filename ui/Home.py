#coding:utf-8
from django.shortcuts import render
from ui.DBManager import getImages,getImagesCount
from config import pageSize,createPages

# 首页
def home(request):
	pageIndex = int(request.GET.get("page", 10))
	images = getImages(pageIndex,pageSize)

	count = getImagesCount()
	res = count % pageSize
	pageCount = count / pageSize

	if res != 0:
		pageCount += 1
	prePage = pageIndex - 1
	if prePage < 1:
		prePage = 1

	nextPage = pageIndex + 1
	if nextPage > pageCount:
		nextPage = pageCount

	pages = createPages(pageCount, pageIndex)
	return render(request,'home.html',{'images':images,'prePage':prePage,'pages':pages,'pageIndex': pageIndex,'count': count,
	                                   'pageCount': pageCount,'nextPage': nextPage, 'pages': pages})
