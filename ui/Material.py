#coding:utf-8
from django.http import HttpResponse

# 素材
def material(request,pageIndex):
	return HttpResponse('素材')