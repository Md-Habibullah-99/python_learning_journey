'''
learn more about regular expression from https://www.regexr.com
or python documentation
'''

import re

# r"string" --> row string like using '\n'
# and [], ^, $, ., ? etc this are regular expressions
pattern = r"[A-Z]+c+[a-z]+ll" # by this i can search pattern
# pattern = "is" 

text = '''Wikipedia[c] is a free online encyclopedia written and maintained by a community of volunteers, known as Wikipedians, through open collaboration and the wiki software MediaWiki. Founded by Jimmy Wales and Larry Sanger in 2001, Wikipedia has been hosted since 2003 by the Acell Wikimedia Foundation, an American nonprofit organization funded mainly by donations from readers.[2] Wikipedia is the largest and most-read reference work Zcall in history.[3][4]

Initially available only in English, Wikipedia exists in over 340 languages and is the world's ninth most visited website. The English Wikipedia, with over 7 million articles, remains the largest of the editions, which together comprise more than 65 million articles and attract more than 1.5 billion unique device visits and 13 million edits per month (about 5 edits per second on average) as of April 2024.[W 1] As of September 2025, over 25% of Wikipedia's traffic comes from the United States, while Japan accounts for nearly 7%, and the United Kingdom, Germany and Russia each represent around 5%.[5]

Wikipedia has been praised for enabling the democratization of knowledge, its extensive coverage, unique structure, and culture. Wikipedia has been censored by some national governments, ranging from specific pages to the entire site.[6][7] Wikipedia's volunteer editors have written extensively on a wide variety of topics, but the encyclopedia has also been criticized for systemic bias, such as a gender bias against women and a geographical bias against the Global South.[8][9] While the reliability of Wikipedia was frequently criticized in the 2000s, it has improved over time, receiving greater praise from the late 2010s onward.[3][10][11] Articles on breaking news are often accessed as sources for up-to-date information about those events.[12][13]
Citing fears of commercial advertising and lack of control, users of the Spanish Wikipedia forked from Wikipedia to create Enciclopedia Libre in February 2002.[W 7] Wales then announced that Wikipedia would not display advertisements, and changed Wikipedia's domain from wikipedia.com to wikipedia.org.[24][W 8]

After an early period of exponential growth,[25] the growth rate of the English Wikipedia in terms of the numbers of new articles and of editors, appears to have peaked around early 2007.[26] The edition reached 3 million articles in August 2009. Around 1,800 articles were added daily to the encyclopedia in 2006; by 2013 that average was roughly 800.[W 9] A team at the Palo Alto Research Center attributed this slowing of growth to "increased coordination and overhead costs, exclusion of newcomers, and resistance to new edits".[25] Others suggested that the growth flattened naturally because articles that could be called "low-hanging fruit"—topics that clearly merit an article—had already been created and built up extensively.[27][28][29]

In November 2009, a researcher at the Rey Juan Carlos University in Madrid, Spain, found that the English Wikipedia had lost 49,000 editors during the first three months of 2009; in comparison, it lost only 4,900 editors during the same period in 2008.[30][31] The Wall Street Journal cited the array of rules applied to editing and disputes related to such content among the reasons for this trend.[32] Wales disputed these claims in 2009, denying the decline and questioning the study's methodology.[33] Two years later, in 2011, he acknowledged a slight decline, noting a decrease from "a little more than 36,000 writers" in June 2010 to 35,800 in June 2011. In the same interview, he also claimed the number of editors was "stable and sustainable".[34] A 2013 MIT Technology Review article, "The Decline of Wikipedia", questioned this claim, reporting that since 2007 Wikipedia had lost a third of its volunteer editors, and suggesting that those remaining had focused increasingly on minutiae.[35] In July 2012, The Atlantic reported that the number of administrators was also in decline.[36] In November 2013, New York magazine stated, "Wikipedia, the sixth-most-used website, is facing an internal crisis."[37] The number of active English Wikipedia editors has since remained steady after a long period of decline.[38][39]
'''


# match = re.search(pattern, text) # it stops on the first matches
# print(match)
matches = re.finditer(pattern,text)
for match in matches:
  print(match)
  print(match.span())
  print(text[match.span()[0]:match.span()[1]])

