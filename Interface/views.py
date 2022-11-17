from django.shortcuts import render
from django.forms.models import model_to_dict
import json

from Question.models import Question, Subject, Topic


# Create your views here.

def homepage(request):
    return render(request, "interface/homepage.html")


def subjectsPage(request):

    subjects = Subject.objects.all()

    context  = {
        "subjects": subjects
    }

    print(f"Context ", context["subjects"])
    return render(request, "interface/subjects.html", context)

def aboutPage(request):
    return render(request, "interface/about.html")

def topicsPage(request, pk):

    subject =  Subject.objects.get(pk=pk)
    topics = Topic.objects.filter(subject=subject)

    context = {
        "topics" : []
    }

    for topic in topics:
        context["topics"].append(topic)

    print("Topics = ", context["topics"])

    # return render(request, "Interface/topics.html", context)
    return render(request, "interface/topics.html", context)

def getQuestions(request, pk):

    topic =  Topic.objects.get(pk=pk)
    questions = Question.objects.filter(topic=topic)

    questionsAsJson = convertArrayToJson(questions)

    context = {
        "questions" : questionsAsJson
    }


    # return render(request, "Interface/topics.html", context)
    return render(request, "interface/old-interface.html", context)

# Indiviudal functions
def convertArrayToJson(array):
    json_objects = []
    for object in array:

        object_dict = model_to_dict(object)
        json_objects.append(object_dict)

    array_json = json.dumps(json_objects)

    return array_json