import pandas as pd


#Q.1 
roll_number=input("Enter your roll no.")
last_two_digits = roll_number[-2:]

categories=["billing", "account",
"general"]

fixed_entries = [
  {"question": "what is the annual fee", "answer": "The annual fee is Rs 500.",
  "keywords": "fee cost price charge", "category": "billing"},
  {"question": "how to reset password", "answer": "Go to Settings > Reset Password.",
  "keywords": "password reset login", "category": "account"},
  {"question": "what are your working hours", "answer": "We are open 9 AM to 5 PM.",
  "keywords": "hours timing open time", "category": "general"},
  {"question": "how can i pay the fee", "answer": "You can pay via UPI, card, or net banking",
  "keywords": "pay payment upi fee", "category": "billing"},
  ]

new_entries=[]

for d in last_two_digits:
    d=int(d)
    category=categories[d%3]

    if category=="billing":
        question="What are the modes for payment?"
        answer="You can find out in the checkout page"
        keywords="payment modes billing checkout"

    elif category=="account":
        question="How do I update my account details?"
        answer="Go to profile page-> settings -> user details"
        keywords="change profile update details"
    else:
        question="Benefits of premium membership?"
        answer="Free and faster delivery; virtualCoins on every purchase."
        keywords="advantages premium coins member"

    new_entries.append(
        {
            "question":question,
            "answer":answer,
            "keywords":keywords,
            "category":category
        }
    )

all_entries=fixed_entries+new_entries

df=pd.DataFrame(all_entries)

print(df)

        

#Q.2

def score_query(query,df):
    
    query_words=set(query.lower().split())

    results=[]

    for index, row in df.iterrows():
        keywords=set(row["keywords"].lower().split())

        matching_words=query_words.intersection(keywords)
        confidence_score=len(matching_words)/len(query_words)

        if(confidence_score>0):
          results.append(
              {
                  "question":row["question"],
                  "answer":row["answer"],
                  "category":row["category"],
                  "confidence_score": confidence_score
              }
          )

    results.sort(key=lambda x:x["confidence_score"], reverse=True)
    return results


query=input("Enter your query: ")
if (not query.strip()):
    print("Empty query")
else :
    print(score_query(query,df))
  
        

            
        

