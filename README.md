Course materials for Applied Natural Language Processing (Spring 2019). 
Syllabus: http://people.ischool.berkeley.edu/~dbamman/info256.html

|Notebook|Description|
|---|---|
|1.words/EvaluateTokenizationForSentiment.ipynb|The impact of tokenization choices on sentiment classification.|
|1.words/ExploreTokenization.ipynb|Different methods for tokenizing texts (whitespace, NLTK, spacy, regex)|
|1.words/TokenizePrintedBooks.ipynb|Design a better tokenizer for printed books|
|2.distinctive_terms/ChiSquare.ipynb|Find distinctive terms using the Chi-square test|
|2.distinctive_terms/CompareCorpora.ipynb|Find distinctive terms using the Mann-Whitney rank sums test|
|3.dictionaries/DictionaryTimeSeries.ipynb|Plot sentiment over time using human-defined dictionaries|
|4.classification/CheckData_TODO.ipynb|Gather data for classification|
|4.classification/FeatureExploration_TODO.ipynb|Feature engineering for text classification|
|4.classification/FeatureWeights_TODO.ipynb|Analyze feature weights for text classification|
|4.classification/Hyperparameters_TODO.ipynb|Explore hyperparameter choices on classification accuracy|
|5.text_regression/Regularization.ipynb|Linear regression with L1/L2 regularization for box office prediction|
|6.tests/BootstrapConfidenceIntervals.ipynb|Estimate confidence intervals with the bootstrap|
|6.tests/ParametricTest.ipynb|Hypothesis testing with parametric (normal) tests|
|6.tests/PermutationTest.ipynb|Hypothesis testing with non-parametric (permutation) tests|
|7.embeddings/DistributionalSimilarity.ipynb|Explore distributional hypothesis to build high-dimensional, sparse representations for words|
|7.embeddings/TFIDF.ipynb|Explore distributional hypothesis to build high-dimensional, sparse representations for words (with TF IDF scaling)|
|7.embeddings/TurneyLittman2003.ipynb|Use word embeddings to implement the method of Turney and Littman (2003) for calculating the semantic orientation of a term defined by proximity to other terms in two polar dictionaries.|
|7.embeddings/WordEmbeddings.ipynb|Explore word embeddings using Gensim|
|8.neural/MLP.ipynb|MLP for text classification (keras)|
|8.neural/ExploreMLP.ipynb|Explore MLP for your data (keras)|
|8.neural/CNN.ipynb|CNN for text classification (keras)|
|8.neural/LSTM.ipynb|LSTM for text classification (keras)|
|8.neural/Attention.ipynb|Attention over word embeddings for document classification (keras)|
|8.neural/AttentionLSTM.ipynb|Attention over LSTM output for text classification (keras)|
|9.annotation/IAAMetrics.ipynb|Calculate inter-annotator agreement (Cohen's kappa, Krippendorff's alpha)|
|10.wordnet/ExploreWordNet.ipynb|Explore WordNet synsets with a simple method for finding in a text all mentions of all hyponyms of a given node in the WordNet hierarchy (e.g., finding all buildings in a text).|
|10.wordnet/Lesk.ipynb|Implement the Lesk algorithm for WSD using word embeddings|
|10.wordnet/Retrofitting.ipynb|Explore retrofit word vectors|
|11.pos/KeyphraseExtraction.ipynb|Keyphrase extraction with tf-idf and POS filtering|
|11.pos/POS_tagging.ipynb|Understand the Penn Treebank POS tags through tagged texts|
|12.ner/ExtractingSocialNetworks.ipynb|Extract social networks from literary texts|
|12.ner/SequenceLabelingBiLSTM.ipynb|BiLSTM + sequence labeling for Twitter NER|
|12.ner/ToponymResolution.ipynb|Extract place names from text, geolocate them and visualize on map|
|13.mwe/JustesonKatz95.ipynb|Implement Justeson and Katz (1995) for identifying MWEs using POS tag patterns|
|14.syntax/SyntacticRelations.ipynb|Explore dependency parsing by identifying the actions and objects that are characteristically associated with male and female characters.|
|15.coref/CorefSetup.ipynb|Install neuralcoref for coreference resolution|
|15.coref/ExtractTimeline.ipynb|Use coreference resolution for the task of timeline generation: for a given biography on Wikipedia, can you extract all of the events associated with the people mentioned and create one timeline for each person?|
|16.ie/DependencyPatterns.ipynb|Measuring common dependency paths between two entities that hold a given relation to each other |
|16.ie/EntityLinking.ipynb|Explore named entity disambiguation and entity linking to Wikipedia pages. |
