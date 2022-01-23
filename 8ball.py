Question = input("Ask a question:\n")
Answerlist = ["Yes", "No", "Yeah", "Nope", "Most likely", "You may rely on it...", "Don't count on it..."]
Answer = __import__("random").choice(Answerlist)
print(f"Question: {Question}\nAnswer: {Answer}") 
