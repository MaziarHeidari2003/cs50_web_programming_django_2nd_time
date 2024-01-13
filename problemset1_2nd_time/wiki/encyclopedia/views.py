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