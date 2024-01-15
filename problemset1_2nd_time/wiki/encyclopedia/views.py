from django.shortcuts import render
import markdown

from . import util


def index(request):
    entries = util.list_entries()
    css_file = util.get_entry("CSS")
    coffee = util.get_entry('coffee')
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)
    

def entry(request,title):
    html_content = convert_md_to_html(title)
    if html_content == None :
        return render(request,"encyclopedia/error.html", {
            "message": "This entry does not exist"
        })
    else:
        return render(request,"encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })
    

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html",{
                "title": entry_search,
                "content": html_content
            })    
        else:
            recommendation = []
            all_entries = util.list_entries()
            for entry in all_entries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request,"encyclopedia/search.html",{
                "recommendation": recommendation
            } )        
        

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")      
    else:
        title = request.POST['title']
        content = request.POST['content']
        title_exist = util.get_entry(title)
        if title_exist is not None :
            return render(request,"encyclopedia/error.html", {
                "message": "Entry page already exists"
            })
        else:
            util.save_entry(title,content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })


def edit(request):
    if request.method == 'POST':
        title = request.POST['entry_tag']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title":title,
            "content": content
        })


def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        html_content = convert_md_to_html(title)
        util.save_entry(title,content)
        return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })
        
