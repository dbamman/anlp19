# Download and install Anaconda environment for Python 3.6

https://www.anaconda.com/download/

# Navigate to your anlp directory and exit out of the anlp conda environment if needed

```sh
conda deactivate
 ```

# Create new anaconda environment with python version 3.6

```sh
conda create --name anlp36 python=3.6
 ```

# Activate environment

```sh
conda activate anlp36
```

# Check version (should be 3.6.8)

```sh
python --version 
```


# Install packages

Be sure to install these specific versions to make debugging easier for everyone in class.

```sh
conda install nb_conda=2.2.1
conda install nltk=3.4
conda install spacy=2.0.12
conda install scikit-learn=0.20.2
conda install matplotlib=3.0.2
conda install pandas=0.24.0
conda install gensim=3.4.0
conda install tensorflow=1.12.0
conda install keras=2.2.4

```

# Install spaCy English model

```sh
python -m spacy download en
```

# Use Jupyter notebooks

That's it! Whenever you're ready to use a Jupyter notebook in this setup, open up the terminal and navigate to the folder containing the notebook; then activate the anlp environment to access these libraries and start up the notebook:

```sh
source activate anlp36
jupyter notebook
```
