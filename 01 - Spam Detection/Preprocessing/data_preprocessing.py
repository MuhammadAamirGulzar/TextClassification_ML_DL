import os , sys
import string
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import demoji
from bs4 import BeautifulSoup
from nltk.stem.porter import PorterStemmer  
from nltk.stem import WordNetLemmatizer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Some preprocessing functions of the data are as follows:
"""
preprocess the data using the following steps: 
1. remove the punctuations
2. remove the stopwords
3. remove the numbers
4. remove the emojis
5. remove the urls
6. remove the html tags
7. remove the extra spaces
8. convert the text to lowercase
9. lemmatize the text
10. remove the words with length less than 2
11. remove the words with length greater than 15
"""

# 1 remove the punctuations using the following function: 
def remove_punctuations(text):
    """ remove punctuations """
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text
# 2 remove the stopwords using the following function:
def remove_stopwords(text):
    """ remove stopwords """
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    return ' '.join(tokens_without_sw)
# 3 remove the numbers using the following function:
def remove_numbers(text):
    """ remove numbers """
    text = re.sub(r'\d+', '', text)
    return text
# 4 remove the emojis using the following function:
def remove_emojis(text):
    """ remove emojis """
    text= demoji.replace(text, '')
    return text
# 5 remove the urls using the following function:
def remove_urls(text):
    """ remove urls """
    text = re.sub(r'http\S+', '', text)
    return text
# 6 remove the html tags using the following function:
def remove_html_tags(text):
    """ remove html tags """
    text = BeautifulSoup(text, 'lxml').get_text()
    return text
# 7 remove the extra spaces using the following function:
def remove_extra_spaces(text):
    """ remove extra spaces """
    text = re.sub(' +', ' ', text)
    return text
# 8 convert the text to lowercase using the following function:
def convert_to_lowercase(text):
    """ convert to lowercase """
    text = text.lower()
    return text
# 9 lemmatize the text using the following function:
def lemmatize_text(text):
    """ lemmatize text """
    lemmatizer = WordNetLemmatizer()
    text_tokens = word_tokenize(text)
    text = ' '.join([lemmatizer.lemmatize(word) for word in text_tokens])
    return text
# 10 remove the words with length less than 2 and greater than 15 using the following function:
def remove_words_with_length_less_than_2_and_greater_than_15(text):
    """ remove words with length less than 2 and greater than 15 """
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if len(word) > 2 and len(word) < 15]
    return ' '.join(tokens_without_sw)

# define a main preprocess data function which will call the required function from above to preprocess the data 
def preprocess_data(text, preprocessing_steps):
    """ preprocess data """
    if preprocessing_steps["remove_punctuations"]:
        text = remove_punctuations(text)
    if preprocessing_steps["remove_stopwords"]:
        text = remove_stopwords(text)
    if preprocessing_steps["remove_numbers"]:
        text = remove_numbers(text)
    if preprocessing_steps["remove_emojis"]:
        text = remove_emojis(text)
    if preprocessing_steps["remove_urls"]:
        text = remove_urls(text)
    if preprocessing_steps["remove_html_tags"]:
        text = remove_html_tags(text)
    if preprocessing_steps["remove_extra_spaces"]:
        text = remove_extra_spaces(text)
    if preprocessing_steps["convert_to_lowercase"]:
        text = convert_to_lowercase(text)
    if preprocessing_steps["lemmatize"]:
        text = lemmatize_text(text)
    if preprocessing_steps["remove_words_with_length_less_than_2 and greater_than_15"]:
        text = remove_words_with_length_less_than_2_and_greater_than_15(text)
    return text
