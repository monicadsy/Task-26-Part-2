from django.shortcuts import render, redirect, get_object_or_404
from .models import Stickynote
from .forms import StickynoteForm


# Create CRUD view for the app
def get_all(request):
    """
    View to display a list of all notes.

    :param request: HTTP request object.
    :return: Rendered template with a list of notes.
    """

    stickynotes = Stickynote.objects.all()

    # Creating a context dictionary to pass data
    context = {
        'stickynotes': stickynotes,
        'page_title': 'Stickynotes',
    }
    return render(request, 'stickynotes/index.html', context)


def get(request, pk):
    """
    View to display details of a specific note.
    :param request: HTTP request object.
    :param pk: Primary key of the post.
    :return: Rendered template with details of the specified post
    """
    stickynote = get_object_or_404(Stickynote, pk=pk)
    return render(request, 'stickynotes/detail.html', {'stickynote':
                  stickynote})


def create(request):
    """
    View to create a new note
    :param request: HTTP request object.
    :return: Rendered template for creating a new post.
    """
    if request.method == 'POST':
        form = StickynoteForm(request.POST)
        if form.is_valid():
            stickynote = form.save(commit=False)
            stickynote.save()
            return redirect('stickynotes')

    else:
        form = StickynoteForm()
    return render(request, 'stickynotes/stickynote_form.html', {'form': form})


def update(request, pk):
    """
    View to update an existing post.

    :param request: HTTP request object.
    :param pk: Primary key of the post to be updated.
    :return: Rendered template for updating the specified post.
    """
    stickynote = get_object_or_404(Stickynote, pk=pk)

    if (request.method == 'POST'):
        form = StickynoteForm(request.POST, instance=stickynote)

        if form.is_valid():
            stickynote = form.save(commit=False)
            stickynote.save()
            return redirect('stickynotes')
    else:
        form = StickynoteForm(instance=stickynote)
    return render(request, 'stickynotes/stickynote_form.html', {'form': form})


def delete(request, pk):
    """
    View to delete an existing post.

    :param request: HTTP request object.
    :param pk: Primary key of the post to be deleted.
    :return: Redirect to teh post list after deletion.
    """
    stickynote = get_object_or_404(Stickynote, pk=pk)
    stickynote.delete()
    return redirect('stickynotes')
