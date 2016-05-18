#coding:utf-8
from django.shortcuts import render
from DBManager import filterImages,getfilterImagesCount
from config import pageSize,createPages

# 灵感
def inspiration(request,pageIndex):
	if pageIndex:
		allCount = pageSize - 2
		pageIndex = int(pageIndex)
		tag = '移动'
		images = filterImages(tag,pageIndex, allCount)

		count = getfilterImagesCount(tag)
		res = count % allCount
		pageCount = count / allCount

		if res != 0:
			pageCount += 1
		prePage = pageIndex - 1
		if prePage < 1:
			prePage = 1

		nextPage = pageIndex + 1
		if nextPage > pageCount:
			nextPage = pageCount

		pages = createPages(pageCount, pageIndex)
		return render(request, 'inspiration.html',
		              {'images': images, 'prePage': prePage, 'pages': pages, 'pageIndex': pageIndex, 'count': count,
	               'pageCount': pageCount, 'nextPage': nextPage, 'pages': pages})
