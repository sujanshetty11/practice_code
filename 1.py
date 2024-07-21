from collections import defaultdict,Counter
import math 

reviews=[
    ("fun,couple,love,love","comedy"),
    ("fast,furious,shoot","action"),
    ("couple,fly,fast,fun,fun","comedy"),
    ("furious,shoot,shoot,fun","action"),
    ("fly,fast,shoot,love","action")

]

D="fast,couple,shoot,fly"

def tokenize(text):
    return text.split(",")

class_doc=defaultdict(list)
vocabulory=set()
class_count=defaultdict(int)

for review , catgory in reviews:
    tokens=tokenize(review)
    class_doc[catgory].extend(tokens)
    
    class_count[catgory] +=1
    vocabulory.update(tokens)

    vocab_size=len(vocabulory)
    total_doc=len(reviews)
    priors={catgory: count /total_doc for catgory ,count in class_count.items()}


likelihood={}

for catgory,tokens in  class_doc.items():
    token_count=Counter(tokens)
    total_words=len(tokens)
    likelihood[catgory]={word : (token_count[word]+1)/ (total_words +vocab_size) for word in vocabulory}
    tokens=tokenize(D)

posterior={}

for catgory in priors :
    log_prob=(priors[catgory])
    for token in tokens:
        log_prob *= (likelihood[catgory].get(token,1/ (len(class_doc[catgory])+vocab_size)))

    posterior[catgory] =log_prob

    most= max(posterior, key=posterior.get)


    print(posterior)
    print(most)
