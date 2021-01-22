from django.shortcuts import render

from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger

from . models import Product



def index(request):

	product = Product.objects.all()

	
	paginator = Paginator(product, 3)
	page_number = request.GET.get('page')
	products = paginator.get_page(page_number)



	
	



	return render(request , 'index.html' , {'products': products } )



def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get( 'name', None)
        if query_name:
            results = Product.objects.filter(name__contains=query_name)
            return render(request, 'product_search.html', {"results":results})

    return render(request, 'product_search.html')
