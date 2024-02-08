from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from item.models import Item
from conversation.models import Conversation

@login_required
def main(request):
    items = get_list_or_404(Item, created_by=request.user)
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    for conversation in conversations:
        membersPlain = conversation.members.values_list("username", flat=True)
        if membersPlain.first() != request.user.username:
            conversation.convo_with = membersPlain.first()
        elif membersPlain.last() != request.user.username:
            conversation.convo_with = membersPlain.last()

    return render(request, 'dashboard/index.html', {
        'items': items,
        'conversations': conversations,
        'user': request.user
    })
