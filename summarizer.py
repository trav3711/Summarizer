import bs4 as bs
import requests
import json
import re
import nltk
import heapq

nltk.download('stopwords')
nltk.download('punkt')

#response = requests.get("https://en.wikipedia.org/wiki/Ip_Man")

#json_data = json.loads(response.text)
#print(json.dumps(json_data, indent=4, sort_keys=True))

#scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Ip_Man')
#article = scraped_data.read()

#parsed_article = bs.BeautifulSoup(article,'lxml')

#paragraphs = parsed_article.find_all('p')

#article_text = ""

def summarize(text, summary_length):

    article_text = text

    # Removing Square Brackets and extra spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)

    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-z]', ' ', article_text )
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

    #print(formatted_article_text)

    # A stopword is a common word like the or be which does not aid in summarization
    stopwords = nltk.corpus.stopwords.words('english')
    #print(stopwords)

    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximun_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/maximun_frequency

    sentence_list = nltk.sent_tokenize(article_text)

    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    summary_sentances = heapq.nlargest(summary_length, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentances)
    return summary
