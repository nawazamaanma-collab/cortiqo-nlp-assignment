import pandas as pd
import random

print("Running improved baseline...")

def generate_mock_data(n=150):
    data = []
    for i in range(n):
        q_types = ["simple", "negation", "long_context", "why_how"]
        q_type = random.choice(q_types)
        
        if q_type == "simple":
            q = "What is the capital of France?"
            true = "Paris"
        elif q_type == "negation":
            q = "Which city is not the capital of France?"
            true = "London"
        elif q_type == "long_context":
            q = "What is one famous landmark mentioned?"
            true = "Eiffel Tower"
        else:
            q = "Why is Python popular?"
            true = "Easy to learn"
        
        pred = true if random.random() > 0.4 else "wrong answer"
        
        data.append({
            'question': q,
            'q_type': q_type,
            'true_answer': true,
            'predicted': pred,
        })
    return pd.DataFrame(data)

def normalize_answer(text):
    if not isinstance(text, str):
        return ""
    text = text.lower().strip()
    text = text.replace("the ", "").replace("a ", "").replace("an ", "")
    return text

def run_baseline():
    df = generate_mock_data()
    df['norm_true'] = df['true_answer'].apply(normalize_answer)
    df['norm_pred'] = df['predicted'].apply(normalize_answer)
    df['exact_match'] = df['norm_true'] == df['norm_pred']
    
    overall = df['exact_match'].mean()
    print(f"Overall Accuracy: {overall:.3f}")
    
    print("\nAccuracy by type:")
    for qtype, group in df.groupby('q_type'):
        acc = group['exact_match'].mean()
        print(f"  {qtype}: {acc:.3f}")
    
    df.to_csv('baseline_results.csv', index=False)
    print("Saved results.")

if __name__ == "__main__":
    run_baseline()
