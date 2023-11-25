from product.models import Category

def base_data(request):
    data = {}
    data["navbar_categories"] = Category.objects.all()
    return data