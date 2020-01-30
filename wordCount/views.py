from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
       #return HttpResponse('Hello world!')
       return render(request, "home.html")


"""def eggs(request):
       #return HttpResponse('eggs are awesome')
       return render(request,"home.html") """

def count(request):
    fulltext = request.GET["fulltext"]
    #print(fulltext)
    wordlist = fulltext.split()
    wordCountDic = {}
    for word in wordlist:
           if word in wordCountDic:
                  #increase existence by one
                  wordCountDic[word] += 1
           else:
                  #add to the dic
                  wordCountDic[word] = 1
    sortedWords = sorted(wordCountDic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {"fulltext": fulltext, "count" :len(wordlist), "sortedWords":sortedWords})

def about(request):
       return render(request, "about.html")



 