import pandas as pd
df = pd.read_csv('baseline_results.csv')
print("Negation accuracy:", df[df['q_type']=='negation']['exact_match'].mean())
print("Simple accuracy:", df[df['q_type']=='simple']['exact_match'].mean())
