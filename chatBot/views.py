from django.shortcuts import render
from django.http import JsonResponse
import spacy
from spacy.matcher import Matcher
nlp=spacy.load('en')
matcher = Matcher(nlp.vocab)
matcher.add("CMD", None,
            [{"LOWER": "docker"}, {"LOWER": "table"}],
            [{"LOWER": "server"}, {"LOWER": "stats"}])

def pre_process(text):
    result=[]
    doc=nlp(text)
    matches = matcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        span = doc[start:end]  # The matched span
        result.append(string_id)
        result.append(span.text)
    return(result)
def match(text):
    query=text
    if 'docker' and 'table' in query:
        return '1'
    elif 'create' and 'hadoop' and 'cluster' in query:
        return '2'
    elif 'launch' and 'instance' in query:
        return '3'
    elif 'vincy' and 'send' and 'SMS' in query:
        return '4'
    elif 'vincy' and 'send' and 'mail' in query:
        return '5'
    elif 'launch' and 's3' in query:
	    pass
    else:
        return '0'
def bot(request,command):
    result=[{'html':'<div id="recieved" class="mdl-color--white mdl-shadow--2dp mdl-cell mdl-cell--12-col mdl-cell-align-right mdl-grid innertext"><p class="innertext">hello</p><script type="text/javascript"> say(\'hello\');</script></div>'}, {'text' : 'hello'}]

    return JsonResponse(result)
