# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:42:35 2020

@author: SREERAM S
"""


from textblob import TextBlob
import emoji
import nltk
nltk.download('punkt')

y = input("Enter \n")
sen = TextBlob(y)
x = sen.sentiment.polarity
x = float(x)
print(x)


#polarit rating
p = -1
q = -0.5
r = 0
s =  0.8
t = 1


print("\n")
if x<q and x>=p:
    print("Worst")
    print(emoji.emojize(":angry_face:"))
elif  x>=q and x<r:
    print("Not Satisfactory")
    print(emoji.emojize(":face_with_steam_from_nose:"))
elif x==r:
    print("Moderate")
    print(emoji.emojize(":neutral_face:"))
elif x>r and x<=s:
    print("Satisfactory")
    print(emoji.emojize(":slightly_smiling_face:"))
elif  x>s and x<=t:
    print("Good and Happy")
    print(emoji.emojize(":beaming_face_with_smiling_eyes:"))
            

print("\n")   
res = len(y.split())
print("total No. of words:\n",str(res))  
print("Word Counts: \n",sen.word_counts)
print("The words are: \n",sen.words)
print("The Sentences are : \n",sen.sentences)
    
