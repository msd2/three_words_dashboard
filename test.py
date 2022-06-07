import pandas as pd
from components import preprocess_text, tokenize_text

df = pd.read_csv('comments.csv')
df['Three words'].apply(preprocess_text.process_string)