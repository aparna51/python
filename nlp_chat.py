from nltk.corpus import wordnet
i=1

def definition ():
    print(new_dict[i].definition())

def examples():
    print(new_dict[i].examples())

while (1):
 key_words=input("\tenter a keyword u want to search for\n")
 new_dict=wordnet.synsets(key_words)
 choice=int(input("\tpress 1 for example, 2 for definition\n"))
 if (choice==1):
     examples()

 if (choice==2):
     definition()

 x=int(input("\tcontinue search? press 1 for same word\n 2 for different word\n 3 to quit\t"))
 if (x==3):
      break
 if(x==2):
      continue
 if(x==1):
      c=int(input("\tenter 1 for examples 2 for def\n"))
      if (c==1):
         #print examples
         examples()

      if (c==2):
         #print definition
         definition()
      y=int(input("\tcontinue search? press 1 for same word\n\t 2 for different word\n\t 3 to quit\t"))
      i=i+1
