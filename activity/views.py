from django.shortcuts import render
from .models import *
import json
# Create your views here.
def activity(request):
    act_inses=Activity.objects.filter(profile=request.user)
    act_inses=Activity.objects.filter(profile=request.user)
    act_inses_c=[i.count for i in act_inses]
    act_inses_a=[i.activity for i in act_inses]
    time=[]
    for i in act_inses:
        time.append(i.time.isoformat())
    context={'act_inses':act_inses,
            'act_inses_c':act_inses_c,
             'act_inses_a':json.dumps(act_inses_a),
             'time':json.dumps(time),
             'reg_time':request.user.date_joined.isoformat()}
    for i in context['act_inses']:
        print(i,i)
    return render(request,"activity.html",context)