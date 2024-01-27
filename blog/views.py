from django.shortcuts import render

# Creating View
def post_list(request):
    return render(request, 'blog/post_list.html', {})
