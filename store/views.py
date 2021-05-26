

from django.shortcuts import get_object_or_404, render
from django.views import View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password

from cart.cart import Cart
from store.models import Product, Category, Image
from store.forms import ProductForm, ImageForm

User = get_user_model()

def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.price, quantity)

def remove_from_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product, quantity)

def get_cart(request):
    return render(request, 'cart.html', {'cart': Cart(request)})




class StoreView(View):
    template_name = 'store.html'

    def get_context(self):
        context = {}
        categories = Category.objects.all()[:6]
        products = Product.objects.all()
        context['products'] = products
        context['categories'] = categories
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context()
        data = request.POST
        if data.get('category'):
            category = Category.objects.get(id=data.get('category'))
            products = Product.objects.filter(category=category)
            context['products'] = products
        if data.get('cost'):
            products = Product.objects.order_by('price')
            context['products'] = products
        if data.get('auth'):
            user = authenticate(request, username=data.get('login'), password=data.get('password'))
            if user is not None:
                login(request, user)
            else:
                context = self.get_context()
                context['error'] = "Неправильные параметры входа. Проверьте логин и пароль."
                return render(request, self.template_name, context)

            if user.profile.perm == "CLI":
                return HttpResponseRedirect('/store/')
            if user.profile.perm == "ADM":
                return HttpResponseRedirect('/store/admin/')

        if data.get('register'):
            user = User.objects.create_user(data.get('login'), data.get('email'), data.get('password'))
            user.profile.phone = data.get('phone')
            user.save()
        if data.get('buy_id'):
            product_id = data.get('buy_id')
            quantity = 1
            add_to_cart(request, product_id, quantity)
        if data.get('delete_id'):
            product_id = data.get('delete_id')
            quantity = 1
            remove_from_cart(request, product_id, quantity)
        return render(request, self.template_name, context)


class AdminView(View):
    template_name = 'admin_editstore.html'
    form = ProductForm

    def get_context(self):
        context = {}
        context['form'] = self.form
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context()
        data = request.POST

        category = Category.objects.get(id=data.get('category'))
        product = Product.objects.create(
            title       = data.get("title"),
            description = data.get("description"),
            price       = data.get("price"),
            amount      = data.get("amount"),
            category    = category,
        )

        if request.FILES.get('image'):
            Image.objects.create(image = request.FILES.get('image'), product=product)

        return render(request, self.template_name, context)


class EditStoreView(View):
    template_name = 'store_editing.html'

    def get_context(self):
        context = {}
        categories = Category.objects.all()[:6]
        products = Product.objects.all()
        context['products'] = products
        context['categories'] = categories
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context()
        data = request.POST
        if data.get('category'):
            category = Category.objects.get(id=data.get('category'))
            products = Product.objects.filter(category=category)
            context['products'] = products
        return render(request, self.template_name, context)


class TableStoreView(View):
    template_name = 'store_table.html'

    def get_context(self):
        context = {}
        products = Product.objects.all()
        context['products'] = products
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context()
        data = request.POST
        print(data)
        return render(request, self.template_name, context)


class CartView(View):
    template_name = 'cart.html'

    def get_context(self, request):
        cart = Cart(request)
        sum = 0
        context = {'cart': cart}
        for item in cart:
            sum += item.unit_price * item.quantity
        context['cart_price'] = sum
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context(request)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        for item in cart:
            product = item.product
            product.selled += item.quantity
            product.amount -= item.quantity
            product.save()
        cart.clear()
        context = self.get_context(request)
        return render(request, self.template_name, context)



class ProductDetailView(View):
    template_name = 'detail_product.html'
    form_product = ProductForm
    form_image = ImageForm

    def get_context(self, request, product):
        context = {}
        images_form = {}
        for image in product.all_images():
            # print(image)
            images_form[self.form_image(instance=image)] = image
        # print(images_form)
        # for image in images_form:
        #     print(image)
        context['product'] = product
        context['images_form'] = product.all_images()
        context['product_form'] = self.form_product(instance=product)
        return context

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        context = self.get_context(request, product)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        data = request.POST

        if data.get('delete'):
            image_id = data.get('delete')
            Image.objects.get(id=image_id).delete()

        if data.get('title'):
            product.title = data.get('title')
            product.description = data.get('description')
            product.price = data.get('price')
            product.amount = data.get('amount')
            product.category = Category.objects.get(id=data.get('category'))
            product.save()

        if request.FILES.get('image'):
            Image.objects.create(image = request.FILES.get('image'), product=product)

        if data.get('delete_product'):
            product.delete()
            return HttpResponseRedirect('/store/edit/')

        context = self.get_context(request, product)
        return render(request, self.template_name, context)


class ProfileView(View):
    template_name = 'client_editProfile.html'

    def get_context(self, request):
        context = {}
        user = request.user
        context['profile'] = user
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context(request)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = request.POST

        user = request.user
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.email = data.get('email')
        user.profile.phone = data.get('phone')
        user.save()

        context = self.get_context(request)
        if data.get('old_password') != "":
            old_password = request.POST.get("old_password")
            new_pass = request.POST.get("new_password")
            if check_password(old_password, user.password):
                user.set_password(new_pass)
                update_session_auth_hash(request, user)
                user.save()
            else:
                context['error'] = "Неправильный пароль"
        return render(request, self.template_name, context)
