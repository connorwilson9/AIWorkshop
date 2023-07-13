model = 2
number_words_predict = 10

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

def to_look(words):
	to_look = ""
	i = len(sentence) - 1
	while(i > (len(sentence) - model)):
		if(i == len(sentence) - 1):
			to_look = sentence[i] + to_look
		else:
			to_look = sentence[i] + " " + to_look
		i = i - 1
	return to_look

corpus = open("book.txt", "r")
all_words = corpus.read().split()
lookup = dict()

model = model + 1
for i in range(len(all_words)- (model - 1)):
	gram = ""
	next_word = ""
	for j in range(model):
		if(j < model - 2):
			gram = gram + all_words[i+j]
			gram = gram + " "
		elif(j < model - 1):
			gram = gram + all_words[i+j]
		elif(j < model):
			next_word = all_words[i+j]
	
	if(gram in lookup):
		lookup[gram].append(next_word)
	else:
		lookup[gram] = [next_word]

print("Write a sentence and press enter (the sentence must have at least "+ str(model - 1) + " words in it):")
sentence = input().split()

response = ""
for i in range(number_words_predict):
	word = most_frequent(lookup[to_look(sentence)])
	response = response + " " + word
	del sentence[0]
	sentence.append(word)

print(response)

