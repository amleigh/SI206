import nltk
from nltk.book import *
import math
import random
# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

print("START*******")

blog=(text2[:150])

text=[]
def spaced(word):
	if word in [",", ".", "?", "!", ":", ";"]:
		return word
	else:
		return " " + word
for i in blog:
	text.append(spaced(i))
print("Here is the text of the first 150 tokens...")
print (''.join(text))

st_blog=' '.join(blog)
new_blog=st_blog
nouns=[]
hold_noun=[]
other=[]
adj=[]
verb=[]
adv=[]
prep=[]
sub_other=[]
new=nltk.pos_tag(blog)
for toke in new:
 	if toke[1] =="NN": #noun
 		nouns.append(toke[0])
 	if toke[1] =="JJ": #adj
 		adj.append(toke[0])
 		other.append(toke[0])
 	if toke[1] =="VBD": #past tense verb
 		verb.append(toke[0])
 		other.append(toke[0])
 	if toke[1] =="RB": #adv
 		adv.append(toke[0])
 		other.append(toke[0])
 	if toke[1] =="IN":
 		prep.append(toke[0])
 		other.append(toke[0]) #Preposition or subordinating conjunction	

replacing=math.trunc(len(nouns)*.15)
i=0
while i < replacing:
	rand_item = random.choice(nouns)
	hold_noun.append(rand_item)
	i+=1
	
for n in hold_noun:
	noun_new= input("Please enter in a noun - ")
	new_blog=new_blog.replace(n, noun_new)

replace_other=math.trunc(len(other)*.10)
i=0
while i < replace_other:
	rand_item = random.choice(other)
	sub_other.append(rand_item)
	i+=1

for n in sub_other:
	if n in verb:
		verb_new= input("Please enter in a past tense verb - ")
		new_blog=new_blog.replace(n, verb_new)
	if n in adj:
		adj_new= input("Please enter in an adjective - ")
		new_blog=new_blog.replace(n, adj_new)
	if n in adv:
		adv_new= input("Please enter in an adverb - ")
		new_blog=new_blog.replace(n, adv_new)
	if n in prep:
		prep_new= input("Please enter in a preposition or subordinatin conjunction - ")
		new_blog=new_blog.replace(n, prep_new)	

words=new_blog.split()
final=[]
for i in words:
	final.append(spaced(i))
print("Here is your final MadLib text...")
print(''.join(final))
	               



print ("\n\nEND*******")
