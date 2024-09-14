#!/usr/bin/env python
# coding: utf-8

# In[45]:


# Etapes 1:
# --------
import spacy
nlp = spacy.load("en_core_web_sm") # Charger le modèle 'en_core_web_sm' (small english model). 
                                   # Dans ce cas, la fonction load() retourne un 'nlp object'


# In[63]:


# Etapes 2:
# --------
file= open("Text_Data.txt","r") # Ouvrir le fichier en lecture
token_list = []                 # Créer une liste pour les tokens
for line in file :
    one_line = nlp(line)        # Faire l'analyse de chaque ligne du fichier via la fonction 'nlp'
    token_list.extend(one_line) # Ajouter la ligne analysée à la liste 'token_list' via la fonction 'extend'
file.close;                     # Fermer le fichier
for token in token_list :       # On peut par exemple afficher les lemmes  de ces tokens
    #print(token.lemma_)    


# In[56]:


# Etapes 3:
# --------
    list_stopwords = list(spacy.lang.en.stop_words.STOP_WORDS) # Récupérer la liste des stopwords
    print(list_stopwords[:])                                   # Affichage des stopwords 


# In[57]:


# Etapes 4:
# --------
ponct = [',','.','!','?','\n',';',':','"','“','”','‘','(',')',"'",'[',']','--','...','/'] # Créer une liste contenant les symboles de ponctuation
list_stopwords.extend(ponct)                                                              # Ajouter les ponctuations à la liste des stopwords
print(list_stopwords[:])                                                                  # Afficher la nouvelle liste


# In[58]:


# Etapes 5:
# --------
token_list_filtred1 = [token for token in token_list if token.text not in list_stopwords] # Eliminer les tokens correspondant aux stopwords


# In[60]:


# Etapes 6:
# --------
token_list_filtred2 = [token for token in token_list_filtred1 # Eliminer les pronoms et les verbes
                       if token.lemma_ !='-PRON-'
                       and token.lemma_ != '-'
                       and token.pos_ != 'VERB'
                      ]
print(token_list_filtred2)                                    # Afficher la nouvelle liste


# In[61]:


# Etapes 7:
# --------
token_list_filtred2_lemma = [token.lemma_ for token in token_list_filtred2] # Récupérer tous les lèmmes de la nouvelle liste des tokens
word_counter = {}                                                           # Créer un dicionnaire
for word in token_list_filtred2_lemma:                                      # Compter le nombre d'apparition de chaque lèmme
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
print(word_counter)                                                         # Afficher le dicionnaire


# In[62]:


# Tri des lèmmes en fonction du nombre d'apparition:
# --------
SortedFiltreLemma=dict();    
list_keys = []            
for key, value in sorted(word_counter.items(), key=lambda item: item[1],reverse=True):
    SortedFiltreLemma[key]=value
    list_keys.append(key)
    print("%s: %s" % (key, value))


# In[54]:


list_keys_filtred=list_keys[0:5]


# In[ ]:




