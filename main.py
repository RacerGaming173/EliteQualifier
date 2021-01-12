from bs4 import BeautifulSoup
import requests
import lxml # Used in BS4 on line 13
import operator
from collections import Counter

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
}
url = 'https://www.reddit.com/r/science'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')

# print(soup.select('.Post')[0].get_text())
# Goal:

# https://www.bestproxyreviews.com/python-web-scraper-tutorial/
number_of_upvotes = []
title = []
number_of_comments = []
word_list = []
clean_list =[]

for item in soup.select('.Post'): 
    try:
        print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text())
        number_of_upvotes.append((item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text()))
        print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
        title.append((item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text()))
        print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text())
        number_of_comments.append(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text())
        print(item.select('._2INHSNB8V5eaWp4P0rY_mE a[href]')[0]['href'])	
        #print(item.select('lrzZ8b0L6AzLkQj5Ww7H1 a[href]')[0]['href'])
        print('----------------------------------------')
       # print(item.select('._1qeIAgB0cPwnLhDF9XSiJM')[0].get_text())
    except Exception as e:
        #raise e
        print('Error')

sorted_title = sorted(title)  #From https://www.kite.com/python/answers/how-to-sort-a-list-alphabetically-in-python
sorted_upvotes = sorted(number_of_upvotes, reverse=True)
sorted_comments = sorted(number_of_comments, reverse=True)

def upvote_conversion(number): # converts number prefixes into their respective numeric equivalents
    if "k" in number:
      converted_number_k = number.replace('k', '00') #From https://www.journaldev.com/23674/python-remove-character-from-string
      new_number_k = converted_number_k.replace('.', '')
      print(new_number_k + " upvotes") 
    elif "m" in number:
      converted_number_m = number.replace('m', '00000')
      new_number_m = converted_number_m.replace('.', '')
      print(new_number_m + " upvotes")
    else:
      print(number + " upvotes")
    print('')

def comment_conversion(number): # converts number prefixes into their respective numeric equivalents
    number_without_comments = number.replace('comments', '')
    if "k" in number:
      converted_number_k = number_without_comments.replace('k', '00') #From https://www.journaldev.com/23674/python-remove-character-from-string
      new_number_k = converted_number_k.replace('.', '')
      print(new_number_k + " comments") 
    elif "m" in number:
      converted_number_m = number_without_comments.replace('m', '00000')
      new_number_m = converted_number_m.replace('.', '')
      print(new_number_m + " comments")
    else:
      print(number + " comments")
    print('')

for number in sorted_upvotes: 
  upvote_conversion(number)



for titles in sorted_title:
  print(titles)
  print('') 

for number in sorted_comments: #Attempt at sorting numbers from greatest to least considering all digits instead of just the first, but unsuccessful
  #number_list = []
  #new_number = number.replace('comments', '')
  #number_list.append(new_number)
  #new_sorted_comments = sorted(number_list, key=lambda new_number: int(new_number[1]), reverse=True) #From https://stackoverflow.com/questions/37242148/how-to-sort-multiple-digit-dictionary-values-from-highest-to-lowest
  comment_conversion(number)
  
  #print(number)
  #print('') 

#Lines 93-123 almost entirely sourced from #https://www.geeksforgeeks.org/python-program-crawl-web-page-get-frequent-words/

def split_titles_into_words(): #divides title into individual words
  for titles in title:
    words = titles.lower().split()
    for word in words:
      word_list.append(word)
  #print(word_list)

def clean_word_list(): # obsolete as of right now, intended to clean words of extra characters
    split_titles_into_words()
    for word in word_list: 
        #symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
        #for i in range (0, len(symbols)): 
        new_word = word.replace('!@#$%^&*()_+={[}]|\;:"<>?., ', '') 
        clean_list.append(new_word)
    #print(clean_list)

def create_dictionary(clean_list): # tally the number of times a word was used and print
    clean_word_list()
    word_count = {} 
      
    for word in clean_list: 
        if word in word_count: 
            word_count[word] += 1
        else: 
            word_count[word] = 1
    print(word_count)
    # c = Counter(word_count) 
    # top = c.most_common(10) 
    # print(top)

create_dictionary(clean_list)