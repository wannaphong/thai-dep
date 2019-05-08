# coding: utf8
import spacy
from pathlib import Path
from spacy import displacy
output_dir="./data2"
nlp = spacy.load(output_dir)
while True:
 text=input("text : ")
 doc = nlp(text)
 print("Dependencies", [(t.text, t.dep_, t.head.text) for t in doc])
 svg = displacy.render(doc, style="dep")
 output_path = Path("./sentence.svg")
 output_path.open("w", encoding="utf-8").write(svg)
