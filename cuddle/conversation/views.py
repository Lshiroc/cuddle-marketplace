from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import Conversation
from item.models import Item

@login_required
def index(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:details', pk=conversations.first().id)
    
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=pk)
    else:
        form = ContactForm()
    

    conversations = Conversation.objects.all()
    return render(request, 'conversation/contact.html', {
        'form': form,
        'conversations': conversations
    })


@login_required
def messages(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

    else:
        form = ContactForm()


    return render(request, 'conversation/messages.html', {
        'conversation': conversation,
        'form': form,
    })