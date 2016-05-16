pageSize = 20


def createPages(pageCount, pageIndex):
	pages = []
	if pageCount > 5:
		if pageIndex >= 3:
			max = pageIndex + 3
			if max >= pageCount:
				max = pageCount + 1
			for i in range(pageIndex - 2, max):
				pages.append(i)
		else:
			for i in range(1, 6):
				pages.append(i)
	else:
		for i in range(1, pageCount + 1):
			pages.append(i)

	return pages
