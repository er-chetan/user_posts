from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect,render
from django.template import loader
from managelist.model import AddPost,Category
import sqlite3


# this is your dashboard

def dashboard(request):
    post_data=AddPost.objects.all()
    cat_data=Category.objects.all()
    template=loader.get_template('dashboard.html')
    content={'post_data_all':post_data,'cat_data_all':cat_data}
    return HttpResponse(template.render(content,request))

# fetch all post
def posts(request):
    post_data=AddPost.objects.all()
    return render(request,"posts.html",{"post_data_all":post_data})

# add your post
def addp(request):
    cat_data=Category.objects.all()
    return render(request,"addpost.html",{"cat_data_all":cat_data})

def addpost(request):
    title=request.POST['title']
    category=request.POST.get('category')
    description=request.POST['description']
    add=AddPost(title=title,category=category,description=description)
    add.save()
    return redirect('/dashboard/')

# add category

def addc(request):
    return render(request,"addcategory.html")

def addcategory(request):
    addcategory=request.POST['addcategory']
    description=request.POST['description']
    add=Category(addcategory=addcategory,description=description)
    add.save()
    return redirect('/dashboard/')

# fetch row for update post
def fetchrow(request,id):
    updaterow=AddPost.objects.get(id=id)
    cat_data=Category.objects.all()
    return render(request,"updatelist.html",{"updaterow":updaterow,'cat_data_all':cat_data})

# update the post 

def updatelist(request,id):
    update=AddPost.objects.get(id=id)
    update.title=request.POST['title']
    update.category=request.POST.get('category')
    update.description=request.POST['description']
    update.save()
    return redirect('/dashboard/')

# delete post
def deleterow(request,id):
    conn=sqlite3.connect('db.sqlite3')
    conn.execute(f'DELETE FROM managelist_addpost where id={id}')
    conn.commit()
    return redirect('/dashboard/')

# fetch row update category

def fetch_category(request,id):
    update_category=Category.objects.get(id=id)
    cat_data=Category.objects.all()
    return render(request,"update_category.html",{"update_category":update_category,'cat_data_all':cat_data})

# update category

def update_category(request,id):
    update_cat=Category.objects.get(id=id)
    update_cat.addcategory=request.POST.get('upcate')
    update_cat.save()
    return redirect('/dashboard/')

# delete category

def delete_category(request,id):
    conn=sqlite3.connect('db.sqlite3')
    conn.execute(f'DELETE FROM managelist_category where id={id}')
    conn.commit()
    return redirect('/dashboard')