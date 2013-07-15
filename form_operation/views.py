#encoding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from form_operation.models import Book

def search(request):
    if 'q' in request.GET and request.GET['q']:  #获得用户输入值
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q) #调用model文件中的Book类方法处理后返回结果
        return render_to_response('search_results.html', #渲染输出模板
            {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')