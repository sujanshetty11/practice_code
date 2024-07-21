from collections import defaultdict,Counter
import math

reviews=[
    ("fun, couple, love, love", "comedy"),
("fast, furious, shoot", "action"),
("couple, fly, fast, fun, fun", "comedy"),
("furious, shoot, shoot, fun", "action"),
("fly, fast, shoot, love", "action")
]

D = "fast, couple, shoot, fly"

def tokenize(text):
    return text.split(",")

class_doc=defaultdict(list)
vocabulory=set()
class_count=defaultdict(int)
for review,catlog in reviews:
    tokens=tokenize(review)
    class_doc[catlog].extend(tokens)
    class_count[catlog] +=1
    vocabulory.update(tokens)

    vocab_size=len(vocabulory)
    total_doc=len(reviews)

    priors={catlog: count / total_doc for catlog,count in class_count.items()} #priors = {catgory: count / total_docs for catgory,count in class_count.items()}

likelihood={}
for catlog,tokens in class_doc.items():
    token_count=Counter(tokens)
    total_word=len(tokens)
    likelihood[catlog]={word : token_count[word]+1 /(total_word+vocab_size)for word in vocabulory}

prioprobalities={}

for catlog in priors:
    log_prob=(priors[catlog])
    for token in tokens:
       log_prob *= (likelihood[catlog].get(token,1/(len(class_doc[catlog])+vocab_size))) # log_prob *= (likelihoods[catgory].get(token, 1 / (len(class_docs[catgory]) + vocab_size)))

prioprobalities[catlog]=log_prob
mostlikeli=max(prioprobalities,key=prioprobalities.get)

print(f" probablity og '{D}' is {prioprobalities} ")
print(f" most repeated is {mostlikeli}")





