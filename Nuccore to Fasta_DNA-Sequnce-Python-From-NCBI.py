#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install biopython  


# Installing the biopython is crutial step, the reading function of the biopython files is SeqIO.
# 

# Then from the https://www.ncbi.nlm.nih.gov/ we can extract the related biomolecular code as FASTA file.

# ## Load important libraries

# In[72]:


from Bio import Entrez
from Bio import SeqIO


# In[75]:


Entrez.email='melda.elmas@outlook.com'


# ## Download and view the Sequence(Nuccore/ FASTA)

# In[83]:


#Data base=nuccore
#Identifier GI number
handle=Entrez.efetch(db='nuccore', id='34577602')


# In[84]:


print(handle.read())


# In[85]:


handle=Entrez.efetch(db='nuccore', id='34577602', rettype='fasta')


# In[87]:


print(handle.read())


# In[88]:


#nucleotide
#identifier: Ascending number
#Output format=Genbank
#Display format=Text


# In[89]:


handle=Entrez.efetch(db='nucleotide', id='NM_001126.2', rettype='genbank', retmode='text')


# In[90]:


print(handle.read())


# ## Dowloading and Exploring Sequences

# In[92]:


#identifier: Ascending number
#Output format=FASTA
#Display format=Text
#data base=nucleotide


# In[112]:


handle=Entrez.efetch(db='nucleotide', id='NM_001126.2', rettype='fasta', retmode='text')


# In[113]:


record=SeqIO.read(handle,'fasta')


# In[114]:


#sequence id
record.id


# In[115]:


#sequence description
record.description


# In[119]:


record.name


# In[121]:


#sequence
seq=record.seq


# In[122]:


print(seq[0:10])


# In[123]:


#length of the mRNA sequence
len(seq)


# In[124]:


print(seq)


# In[ ]:


#identifier: Ascending number
#Output format=genbank
#Display format=Text
#data base=nucleotide


# In[125]:


handle=Entrez.efetch(db='nucleotide', id='NM_001126.2', rettype='gb', retmode='text')


# In[126]:


record=SeqIO.read(handle,'gb')


# In[127]:


record.id


# In[129]:


features=record.features


# In[130]:


len(features)


# In[132]:


seq=record.seq


# In[133]:


print(len(seq))


# ## Now, you can download multiple genomes

# In[135]:


handle=Entrez.efetch(db='nuccore', id='3457706,186972394', rettype='fasta')


# In[136]:


print(handle.read())


# In[137]:


handle=Entrez.efetch(db='nuccore', id='3457706,186972394', rettype='fasta')


# In[138]:


records=SeqIO.parse(handle,'fasta')


# In[139]:


records=[i for i in records]


# In[141]:


len(records)


# In[146]:


first_record=records[0]
second_record=records[1]


# In[148]:


first_record.id


# In[149]:


second_record.id


# In[168]:


handle=Entrez.efetch(db='nucleotide', id='34577062', rettype='gb')
record=SeqIO.read(handle,'gb')
outputname='/home/kobina/Desktop/ADSS.gb'

