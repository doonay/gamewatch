# Сначала ставим pycurl https://qna.habr.com/q/648945
from grab import Grab

g = Grab(log_file='out.html')
print(g)
g.go('https://gamer-info.com')

print(g.xpath_text('//title'))