# -*- coding: utf-8 -*-
"""
Created on Fri May 22 01:16:13 2020

@author: User
"""

from collections import defaultdict
import math
import glob
import sys,re
from functools import reduce
import mymodule
synonymwrd=mymodule.importing_files_for_synonymes()
stopwordsl=mymodule.importing_files_for_stopwords()
normalletter=mymodule.importing_files_for_charnormalization()
shorttermstr=mymodule.importing_files_for_shorttermnormalization()
characters = " .,!#$%^&*();:\n\t\\\"?!{}[]<>"
coll=[]
text_file = open("vocabulary.txt", "w+",encoding="utf8")
doc_id = open("docid.txt", "w+",encoding="utf8")
file_folder = 'data/*'
docid=0
for file in glob.glob(file_folder):
    docid=docid+1
    fname = file
    doc_id_name=str(docid)+"   "+fname+"\n"
    doc_id.write(doc_id_name)
    

    file = open(file , "r",encoding="utf8")
    document = file.read()
    terms = document.split()
    for term in terms:
        term_count=terms.count(term)
#        if term=='':
#            continue
#        else:
#            term_with_size=term+" "+str(term_count)+" "+str(docid)+" "
#            for term_with_size_with_docid in coll:
#                if term_with_size_with_docid==term_with_size:
#                    print(term_with_size_with_docid)
#            
#            
#            coll.append(term_with_size);
        for nrml in range(0,len(normalletter)-1,2):
            term = re.sub(normalletter[nrml],normalletter[nrml+1], term)
        for shrttrm in range(0,len(shorttermstr)-1,2):
            term=re.sub(shorttermstr[shrttrm],shorttermstr[shrttrm+1],term)
        for stw in stopwordsl:
            term = re.sub(stw,'', term)
        if len(term)>=2:
            input2=re.match("(.+)(ባቸው|ዉያን|ቸውን|መንት)",term)
            input2=re.match("(.+)(ዎች|ነቷ|ችሁ|ቸው|ኛው|ዎቹ|ኞች|ችን|ዋል|ዬው|ጆች)",term) if not input2 else input2   
            input2=re.match("(.+)(ና|ነት|ኛ|ም|ን|ና|ኦ|ዊ|ች|፣|፡፡|፡|“|”|::|፤|!|!!!|!!|0|1|2|3|4|5|6|7|8|9|01|2016)",term)if not input2 else input2 
            if input2:
                input2.group(1)+'-'+input2.group(2)
                if len(input2.group(1))>=2:
                    input2=input2.group(1)
                else:
                   continue
#                 
            else: input2=term
        else:input2=term
        term=input2
        
        if len(term)>=2:
            input2=re.match("(እንደ|እገሌ|እየ|አስ|ስለ|የተ|በ|ለ|ከ|የ)(.+)",term)
            if input2:
                input2.group(1)+'-'+input2.group(2)
                if len(input2.group(2))>=2:
                    input2=input2.group(2)
                else:
                   continue
            else: input2=term
        else:input2=term
        term=input2 
        for syn in range(0,len(synonymwrd)-1,2):
            term = re.sub(synonymwrd[syn+1],synonymwrd[syn], term)
        term=term.strip(characters)
        
        if term=='':
            continue
        else:
            term_with_size=term+" "+str(term_count)+" "+str(docid)+" "
            coll.append(term_with_size);
#            for term_with_size_with_docid in coll:
#                if term_with_size_with_docid!=term_with_size:
##                    print(term_with_size_with_docid)
#                else:
#                    continue
    dictt = ' '.join([str(elem) for elem in coll]); 
    term_with_doc_name=fname+"   "+dictt+"  \n";
    
    
    
    
    text_file.write(term_with_doc_name)
    
doc_id.close()
text_file.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#    terms = tokenize(document,fname)
#    unique_terms = set(terms)
#    print(unique_terms)














