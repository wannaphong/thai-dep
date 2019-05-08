# coding: utf8
from io import open
from conllu import parse_incr

TRAIN_DATA = []
def is_root(t):
 if t=="root":
  return "ROOT"
 else:
  return t

data_file = open("th_pud-ud-test.conllu", "r", encoding="utf-8")
for tokenlist in parse_incr(data_file):
 wordlist=[]
 head=[]
 deps=[]
 for count, item in enumerate(tokenlist):
  wordlist.append(item["form"])
  head.append(int(item["head"]))
  deps.append(is_root(item["deprel"]))
 TRAIN_DATA.append((" ".join(wordlist),{"heads":head,"deps":deps},),)#,

def get_data():
 return TRAIN_DATA
