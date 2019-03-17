from nltk.corpus import stopwords
import nltk
import re
import os

nltk.download('stopwords')

folder = "."
sub = "[^a-zA-Z' ]+"


def uniqueWords(file_name):
	file = open(folder+"/"+file_name, "r")
	file_lines = file.readlines()
	count_dict = {}
	unique_set = set()
	for l in file_lines:
		l_list = l.split()
		for i in range(len(l_list)):
			l_list[i] = re.sub(sub, '', l_list[i])
		for word in l_list:
			if word not in unique_set and word not in stopwords.words('english'):
				count_dict[word] = 0
				unique_set.add(word)
			if word in unique_set:
				count_dict[word] += 1

	out_name = file_name + "_unique_words"
	print(file_name, "has", len(unique_set), "words!")
	out_file = open(out_name, "w")
	for word in unique_set:
		out_file.write("{} {}\n".format(word, count_dict[word]))
	out_file.close()
	file.close()


# i = 0
# for root, dirs, files in os.walk(folder):
# 	for f in files:
# 		print(i)
# 		i+= 1

if __name__ == "__main__":
	uniqueWords("Shakespeare_all_works")