from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import PetitionForm
from .models import Petition, Vote

def petition_list(request):
    qs = Petition.objects.all().select_related("created_by")
    return render(request, "petitions/petition_list.html", {"petitions": qs})

def petition_detail(request, slug):
    petition = get_object_or_404(Petition.objects.select_related("created_by"), slug=slug)
    user_has_voted = petition.has_voted(request.user)
    return render(request, "petitions/petition_detail.html", {
        "petition": petition,
        "user_has_voted": user_has_voted,
    })

@login_required
def petition_create(request):
    if request.method == "POST":
        form = PetitionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            messages.success(request, "Petition created.")
            return redirect("petitions:detail", slug=obj.slug)
    else:
        form = PetitionForm()
    return render(request, "petitions/petition_form.html", {"form": form})

@require_POST
@login_required
def petition_vote(request, slug):
    petition = get_object_or_404(Petition, slug=slug)
    # Ensure exactly one "yes" vote per user
    vote, created = Vote.objects.get_or_create(petition=petition, user=request.user)
    if created:
        messages.success(request, "Your ‘Yes’ vote has been recorded.")
    else:
        messages.info(request, "You had already voted ‘Yes’ for this petition.")
    return redirect("petitions:detail", slug=petition.slug)