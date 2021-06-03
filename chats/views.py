from django.shortcuts import render, redirect ,get_object_or_404 , HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from plotly.offline import plot
from plotly.graph_objs import Scatter,Pie
import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'


# from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import pickle
# Create your views here.

@login_required
def view_chats(request):

    if request.method == 'POST':
        users = User.objects.all()
        l=[]
        for user in users:
            if not (Chat.objects.filter(user1=user, user2=request.user) | Chat.objects.filter(user1=request.user, user2=user)):
                l.append(user)
        
        return render(request, 'chats/new_chat.html',{'users':l})

    chat = Chat.objects.filter(user1=request.user) | Chat.objects.filter(user2=request.user)
    return render(request, 'chats/view_chats.html',{'all_chat': chat })

def detail_chat(request,username):
    
    sender = request.user
    receiver = User.objects.filter(username=username).first()

    chat = Chat.objects.filter(user1=sender, user2=receiver) | Chat.objects.filter(user1=receiver, user2=sender)

    chat = chat.first()
    if request.method == 'POST':
        
        msg_tosend = request.POST.get("textmsg")
        msg_tosave = Message.objects.create(chat=chat,user=sender,data=msg_tosend)
        msg_tosave.save()

        print(msg_tosend)
    
    # print(chat)
    # if chat:
    if not chat:
        chat = Chat.objects.create(user1=sender,user2=receiver)
        chat.save()


    msgs = Message.objects.filter(chat = chat).order_by("date")
    print(msgs)
    
     # else:
    #     if not chat:
    #         chat = Chat.objects.create(user1=sender,user2=receiver)
    #         chat.save()
        # return HttpResponse(request,'Hi')

    return render(request, 'chats/detail_chats.html',{'msgs': msgs })
   

def make_graph(request):

    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]

    plot_div = plot([Scatter(x=x_data, y=y_data, mode='lines', name='test', opacity=0.8, marker_color='green')],output_type='div')


    labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
    values = [4500, 2500, 1053, 500]
    # fig = px.pie(df, values='tip', names='day')
    plot_div2 = plot([Pie(labels=labels, values=values)],output_type='div')

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    labels = ["Asia", "Europe", "Africa", "Americas", "Oceania"]

    fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                        subplot_titles=['1980', '2007'])
    fig.add_trace(go.Pie(labels=labels, values=[4, 7, 1, 7, 0.5], scalegroup='one',
                        name="World GDP 1980"), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[21, 15, 3, 19, 1], scalegroup='one',
                        name="World GDP 2007"), 1, 2)

    fig.update_layout(title_text='World GDP')

    graph2 = fig.to_html(full_html=False, default_height=500, default_width=700)

    animals=['giraffes', 'orangutans', 'monkeys']

    fig2 = go.Figure(data=[
        go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
        go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
    ])
    # Change the bar mode
    # fig2.update_layout(barmode='group')   #side by side karna hai toh ye
    fig2.update_layout(barmode='stack')

    graph3 = fig2.to_html(full_html=False, default_height=500, default_width=700)

    
    import numpy as np
    np.random.seed(1)

    N = 100
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N) - 5

    # Create traces
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=random_x, y=random_y0,
                        mode='lines',
                        name='lines', line = dict(color='royalblue', width=4, dash='dash')))
    fig3.add_trace(go.Scatter(x=random_x, y=random_y1,
                        mode='lines+markers',
                        name='lines+markers'))
    fig3.add_trace(go.Scatter(x=random_x, y=random_y2,
                        mode='markers', name='markers'))

    # fig3.show()

    graph4 = fig3.to_html(full_html=False, default_height=500, default_width=700)


    return render(request, "chats/graphs.html", context={'plot_div': plot_div,'plot_div2': plot_div2,'graph2': graph2, 'graph3': graph3, 'graph4': graph4})
