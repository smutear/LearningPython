import re

def filter_emoji(text):
	try:
		highpoints = re.compile(u'[\U00010000-\U0010ffff]')
	except re.error:
		highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
	return highpoints.sub(u'',text)


if __name__ == '__main__':
	f = open("E:\\xg_tmp.exp","r")

	text = f.read()
	print text
	print "--------------------------------"
	print "--------------------------------"
	print "--------------------------------"
	t = filter_emoji(text)

	print t