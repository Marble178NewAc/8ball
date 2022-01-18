Question = input("Ask a question:\n")
Answerlist = ["Yes", "No"]
Answer = __import__("random").choice(Answerlist)
print(f"Question: {Question}\nAnswer: {Answer}") 
