from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing
from sklearn import linear_model

class TokenizationTest():

	def __init__(self, trainFile, devFile):
		self.trainFile=trainFile
		self.devFile=devFile

	def read_data(self, filename, tokenizer):
		corpus=[]
		Y=[]
		with open(filename, encoding="utf-8") as file:
			for idx,line in enumerate(file):
				cols=line.rstrip().split("\t")
				label=cols[0]
				text=cols[1]
				tokens=' '.join(tokenizer(text))
				corpus.append(tokens)
				Y.append(label)

		return corpus, Y

	def evaluate(self, tokenizer):
		
		train_corpus, train_labels=self.read_data(self.trainFile, tokenizer)
		dev_corpus, dev_labels=self.read_data(self.devFile, tokenizer)
		
		vectorizer = CountVectorizer(max_features=10000, analyzer=str.split, lowercase=False, strip_accents=None, binary=True)
		X_train = vectorizer.fit_transform(train_corpus)
		X_dev = vectorizer.transform(dev_corpus)

		le = preprocessing.LabelEncoder()
		le.fit(train_labels)

		Y_train=le.transform(train_labels)
		Y_dev=le.transform(dev_labels)

		logreg = linear_model.LogisticRegression(C=1.0, solver='lbfgs', penalty='l2')
		logreg.fit(X_train, Y_train)
		print("Function '%s' Accuracy: %.3f" % (tokenizer.__name__, logreg.score(X_dev, Y_dev)))



