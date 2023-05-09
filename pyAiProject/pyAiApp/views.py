from django.shortcuts import render, HttpResponse,redirect
import os
import openai

def index(request):
    return render(request,"index.html")

def chatGpt(request):
    return render(request,"chatGpt.html")

def openAiChatGpt(request):
    openai.api_key = "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"
    data_in=request.POST['chatData']

        
    completion=openai.Completion.create(
            engine='text-davinci-003',
            prompt=data_in,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
    data_out=completion.choices[0].text
    print(data_out)
    request.session['data_out']=data_out
    return redirect('/chatGpt')    

def transaltor(request):
    return render(request,"translate.html")

def openAiTransaltor(request):
    openai.api_key = "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"
    data_in=request.POST['translateData']
    print(data_in)
        
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=data_in,
    temperature=0.3,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    data_out=response.choices[0].text
    print(data_out)
    request.session['dataTranslate_out']=data_out
    return redirect('/transaltor')    


def jsToPython(request):
    return render(request,"jsToPython.html")

def openAiJsToPython(request):
    openai.api_key = "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"
    data_in=request.POST.get('JStoPythonData')
    #['JStoPythonData']
    print(data_in)
        
    response = openai.Completion.create(
    model="code-davinci-002",
    prompt="#JavaScript to Python:\nJavaScript: \n {data_in}",
    temperature=0,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    data_out=response.choices[0].text
    print(data_out)
    request.session['JStoPython_out']=data_out
    return redirect('/jsToPython')    
