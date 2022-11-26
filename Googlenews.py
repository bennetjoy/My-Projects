from GoogleNews import GoogleNews

googlenews = GoogleNews()
googlenews.setlang('en')
googlenews.setperiod('d')
googlenews.setTimeRange('02/06/202','07/06/2021')
googlenews.setencode('utf-8')
print(googlenews.search('covid'))
googlenews.getpage(2)
googlenews.result() #to get full data
googlenews.gettext() #to get title 
googlenews.clear()