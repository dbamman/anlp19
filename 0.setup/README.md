# Download and install Anaconda environment for Python 3.7

https://www.anaconda.com/download/

# Create new anaconda environment for this class
```sh
conda create --name anlp
 ```

# Activate environment

```sh
source activate anlp
```

# Check version (should be 3.7.1)

```sh
python --version 
```
https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html

# Install packages

Be sure to install these specific versions to make debugging easier for everyone in class.

```sh
conda install nb_conda=2.2.1
conda install nltk=3.4
conda install spacy=2.0.12
conda install scikit-learn=0.20.2
conda install pandas=0.24.0
conda install matplotlib=3.0.2
```

# Install spaCy English model

```sh
python -m spacy download en
```

# Use Jupyter notebooks

That's it! Whenever you're ready to use a Jupyter notebook in this setup, open up the terminal and navigate to the folder containing the notebook; then activate the anlp environment to access these libraries and start up the notebook:

```sh
source activate anlp
jupyter notebook
```

We'll be using Jupyter notebooks extensively in this class; if you're new to them, check out the tutorial here:

* [Jupyter notebook tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)

If you haven't used Github before, you'll just need it to pull course materials (notebooks, data) from the anlp repo.

* [Install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* ` git clone git@github.com:dbamman/anlp19.git`
* Whenever you want to update your local copy: `git pull`

See here for an intro to Git/Github:


* https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners


