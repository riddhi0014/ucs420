import pandas as pd

roll_number=1024170181
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

        


