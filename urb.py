import urllib2
import re
from random import randint

char1 = "A"
char2 = "B"

word1 = urllib2.urlopen("http://www.urbandictionary.com/popular.php?character=" + char1).read()
word1 = re.findall(r'term=(.*)"', word1)
word1 =  word1[randint(0,100)]
word1 = word1.replace('%20', '')
word1 = word1.replace('%27', '')
w1=word1

word1 = urllib2.urlopen("http://www.urbandictionary.com/popular.php?character=" + char2).read()
word1 = re.findall(r'term=(.*)"', word1)
word1 =  word1[randint(0,100)]
word1 = word1.replace('%20', '')
word1 = word1.replace('%27', '')
print w1+word1
