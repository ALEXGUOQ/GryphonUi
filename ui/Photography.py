#coding:utf-8
from django.http import HttpResponse

# 摄影
def photography(request,pageIndex):
	return HttpResponse('摄影')