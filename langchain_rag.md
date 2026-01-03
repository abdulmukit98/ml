1.
````
python3 -m venv venv
source venv/bin/activate
````
2.
````
rm -rf ~/.cache/pip
mkdir -p ~/pip_tmp
export TMPDIR=~/pip_tmp
````
3.
````
pip install pypdf
pip install faiss-cpu
pip install sentence-transformers
pip install langchain
pip install langchain-community
pip install langchain-text-splitters
````
