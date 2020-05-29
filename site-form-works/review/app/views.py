from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import FormView

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


class ProductView(FormView):

    template_name = 'app/product_detail.html'
    form_class = ReviewForm

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        product = get_object_or_404(Product, id=kwargs['pk'])
        reviews = Review.objects.filter(product=product)
        context['product'] = product
        context['reviews'] = reviews
        reviewed_products = request.session.get('reviewed_products') or []
        is_review_exist = True if kwargs['pk'] in reviewed_products else False
        context['is_review_exist'] = is_review_exist
        return self.render_to_response(context)

    def form_valid(self, form):
        feed = form.save(commit=False)
        product = get_object_or_404(Product, id=self.kwargs['pk'])
        feed.product = product
        feed.save()

        reviewed_products = self.request.session.get('reviewed_products') or []
        reviewed_products.append(self.kwargs['pk'])
        self.request.session['reviewed_products'] = reviewed_products
        return redirect(reverse('main_page'))
