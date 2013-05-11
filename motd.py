from bs4 import BeautifulSoup
from mechanize import Browser
import re, rdflib

class rhinoMotd:
	def message(self):
		return self.weatherMessage()
	def zoobornMessage(self):
		return ""
	def weatherMessage(self):
		url = 'http://open.live.bbc.co.uk/weather/feeds/en/2637487/observations.rss'
		br = Browser()
		br.set_handle_robots(False)
		page = br.open(url)
		xml = page.read()
		itemr = re.compile('<item>(.*?)</item>', re.DOTALL)
		descr = re.compile('<description>(.*?)</description>', re.DOTALL)
		tempr = re.compile('([0-9]+)..C')
		tempintr = re.compile('[0-9]+')
		item = str(itemr.search(xml).group(0))
		desc = str(descr.search(item).group(0))
		temp = str(tempr.search(desc).group(0))
		tempint = int(tempintr.search(temp).group(0))
		if tempint<14:
			rv = "Brr! It's a bit cold for rhinos in Southampton! We're used to far higher temperatures in southern Africa!"
		elif tempint<20:
			rv = "I'm quite liking the weather today, it's like a cool winter's day in southern Africa."
		elif tempint<=26:
			rv = "I'm quite liking the weather today, it's nice and warm, just like it is back home!"
		else:
			rv = "Ooh, it's hot today! My thick rhino skin can't take much more!"
		return rv

if __name__ == '__main__':
	rhino = rhinoMotd()
	msg = rhino.message()
	print msg
