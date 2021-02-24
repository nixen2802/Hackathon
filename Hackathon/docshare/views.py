from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from django.core.files.storage import FileSystemStorage


def post(request):
    if request.method=="POST":
        uploaded_file = request.FILES['uploaded_file']
        year=request.POST['year']
        branch=request.POST['branch']
        category=request.POST['category']
        File_name=request.POST['File_name']
        subject =request.POST['subject']
        fs = FileSystemStorage()
        uploaded_file_url =fs.save(uploaded_file.name,uploaded_file)
        student_upload=Post(year=year,branch=branch, category=category, File_name=File_name, subject=subject,uploaded_file=uploaded_file)
        student_upload.save()
      
    return render(request,'docshare/post.html')

def home(request):
    post_id = Post.objects.all()
    params = {'post_id': post_id}
    return render(request, 'docshare/home.html', params)


def about(request):
    return render(request, 'docshare/about.html')

# models.FileField(upload_to=settings.MEDIA_ROOT, null=True)
