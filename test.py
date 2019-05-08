# coding: utf8
import spacy
output_dir="./data2"
nlp = spacy.load(output_dir)
while True:
 text=input("text : ")
 doc = nlp(text)
 print("Dependencies", [(t.text, t.dep_, t.head.text) for t in doc])
