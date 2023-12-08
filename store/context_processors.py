from .models import Category


def allCategories(request):
    categories = Category.getAllCategories()
    return {
        'categories': categories
    }