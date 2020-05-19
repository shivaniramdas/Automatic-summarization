import argparse

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

def main():
	args = parse_arguments()
	content = read_file(args.filepath)
	content = sanitize_input(content)

	sent_tokens, word_tokens = tokenize_content(content)
	sent_ranks = score_tokens(sent_tokens, word_tokens)
	print(summarize(sent_ranks, sent_tokens, args.length))

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('filepath', help='File name of text to summarize')
	parser.add_argument('-l', '--length', default=4, help='No. of sentences to return')
	args = parser.parse_args()
	return args

def read_file(path):
	try:
		with open(path, 'r') as f:
			return f.read()
	except IOError as e:
		print('File could not be located')

def sanitize_input(data):
	replace = {
		ord('\f') : ' ',
		ord('\t') : ' ',
		ord('\n') : ' ',
		ord('\r') : None
	}
	return data.translate(replace)

def tokenize_content(content):

	stop_words = set(stopwords.words('english') + list(punctuation))
	words = word_tokenize(content.lower())
	return (sent_tokenize(content), [word for word in words if word not in stop_words])

def score_tokens(sent_tokens, word_tokens):
	word_freq = FreqDist(word_tokens)
	rank = defaultdict(int)
	for i, sent in enumerate(sent_tokens):
		for  word in word_tokenize(sent.lower()):
			if word in word_freq:
				rank[i] += word_freq[word]

	return rank

def summarize(ranks, sentences, length):

	if int(length) > len(sentences):
		print('You requested more sentences in the summary than there are in the text.')
		return ''

	else:
		indices = nlargest(int(length), ranks, key=ranks.get)
		final_summary = [sentences[j] for j in indices]
		return ' '.join(final_summary)

if __name__ == '__main__':
main()
