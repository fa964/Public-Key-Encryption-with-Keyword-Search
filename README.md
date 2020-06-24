# Public-Key-Encryption-with-Keyword-Search
Based upon construction #2 from the following research paper: https://crypto.stanford.edu/~dabo/papers/encsearch.pdf

pip install pycryptodome
https://pycryptodome.readthedocs.io/en/latest/src/introduction.html

add/remove comment around KeyGen.key_gen() to generate key pairs
it will generate 1 key pair for each word in keywords.txt

alternative is to run KeyGen.py by itself first

after keys are generated, choice a 'keyword' (ie: public key) to encrypt with by choosing the public_key_filename

trapdoor is the trapdoor/private key you wish to test with.
using the correct coresponding trapdoor will return yes. Otherwise no.
