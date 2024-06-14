# uses newspaper4k: https://github.com/AndyTheFactory/newspaper4k
import newspaper

article = newspaper.article(
    'https://realpython.com/learning-paths/data-science-python-core-skills/')

article.nlp()
keywords = article.keywords  # list
summary = article.summary  # text
