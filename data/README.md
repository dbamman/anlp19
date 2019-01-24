# Data

## trump_tweets.json 

A dump of Trump's tweets from http://www.trumptwitterarchive.com/archive, downloaded 1/19/19.

## {dem,repub}.convote.txt

Congressional speech data from http://www.cs.cornell.edu/home/llee/data/convote.html.  Original data processed to yield these files with the following commands:

`find data_stage_three/training_set -name "*_R*" -exec cat {} > repub.convote.txt \;`

`find data_stage_three/training_set -name "*_D*" -exec cat {} > dem.convote.txt \;`

## sentiment.1000.{train,dev}.txt

A sample of 1000 documents + {pos,neg} sentiment labels from the Large Movie Review Dataset http://ai.stanford.edu/~amaas/data/sentiment/

## darwin_origin_ia.txt

OCR'd text of Darwin's Origin of Species, from the Internet Archive https://archive.org/download/originofspecies00darwuoft/originofspecies00darwuoft_djvu.txt
