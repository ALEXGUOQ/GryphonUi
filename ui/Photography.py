#coding:utf-8
from django.shortcuts import render
from ui.DBManager import getPhotos,getPhotosCount
from config import pageSize,createPages

# 摄影
def photography(request,pageIndex):
	if pageIndex:
		pageIndex = int(pageIndex)
		images = getPhotos(pageIndex, pageSize)

		count = getPhotosCount()
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
		return render(request, 'photography.html',
		              {'images': images, 'prePage': prePage, 'pages': pages, 'pageIndex': pageIndex, 'count': count,
		               'pageCount': pageCount, 'nextPage': nextPage, 'pages': pages})