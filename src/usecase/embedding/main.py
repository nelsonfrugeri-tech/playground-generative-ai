from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk

# Baixar os recursos necessários do NLTK
nltk.download('punkt')
nltk.download('punkt_tab')

# Texto de exemplo
text = """ 
O que é embedding? Embedding é uma técnica de aprendizado de máquina que mapeia palavras ou frases para vetores de números reais.
"""

# Tokenizar o texto em palavras
tokens = word_tokenize(text.lower())

# Criar o modelo Word2Vec
model = Word2Vec([tokens], vector_size=50, window=5, min_count=1, workers=4)

# Obter o embedding de uma palavra
word_embedding = model.wv['embedding']
print(f"Embedding da palavra 'embedding':\n{word_embedding}")
