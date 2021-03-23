import re
from collections import defaultdict

def solution(word, pages):
    base_score_dict = {}
    link_score_dict = defaultdict(int)
    a_parser = re.compile('a href = "(.+)*"')

    for idx, page in enumerate(pages):
        page_url = page.split('<meta property=\"og:url\" content=\"')[1].split('\"')[0]
        body_text = page.split('<body>')[1].split('</body>')[0]
        a_hrefs = []
        for link_long in page.split('<a href=\"')[1:]:
            a_hrefs.append(link_long.split('">')[0])

        body_text = re.sub('[^a-z]+', '../../..', body_text.lower()).split('.')
        base_score = len(list(filter(lambda x:x==word.lower(),body_text)))
        base_score_dict[page_url] = (base_score,idx)

        for a_href in a_hrefs:
            link_score_dict[a_href] += (base_score/len(a_hrefs))

    score = []

    for key, values in base_score_dict.items():
        base_score = values[0]
        idx = values[1]
        link_score = link_score_dict[key]
        score.append((idx, base_score+link_score))

    return sorted(score, key = lambda x : (x[1],-x[0]), reverse=True)[0][0]


word = "blind"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

print(solution(word,pages))