from django.contrib.auth.forms import UserCreationForm
from .services import get_all_movies, get_all_series, search_content
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def catalog(request):
    movies = get_all_movies()
    series = get_all_series()
    return render(request, 'pages/catalog.html', {'movies': movies, 'series': series})

def series(request):
    series=get_all_series()
    return render(request, 'pages/series.html', {'series': series} )

def movies(request):
    movies = get_all_movies()
    return render(request, '' \
    'pages/movies.html', {'movies': movies})

def search(request):
    query = request.GET.get('q', '').strip()
    movie_results = []
    series_results = []

def register(request):
    return render(request, 'streamsync_register.html',{
        'form': UserCreationForm
    })

def login(request):
    return render(request, 'login.html')
    if query:
        results = search_content(query)
        movie_results = [item for item in results if item.get('content_type') == 'movie']
        series_results = [item for item in results if item.get('content_type') == 'series']
        return render(request, 'pages/search.html', {
            'query' : query,
            'movies': movie_results,
            'series': series_results,
            'result_count': len(results)
        })
    
    return render(request, 'pages/search.html', {'query': ''})



def content_detail(request, ctype, cid):   
    
    if ctype == 'series':
        data = get_all_series()
    else:
        data = get_all_movies()
    content = next((item for item in data if str(item.get('id')) == str(cid)), None)
    # ... render
    if content:
        return render(request, 'pages/content_view.html', {'content': content})
    else:
        return render(request, 'pages/home.html', status=404)



def main(request):
    return render(request, 'pages/main.html')

@login_required
def login_redirect(request):
    user = request.user

    if user.is_superuser or user.groups.filter(name='administrator').exists():
        return redirect('app:movies') #provisional redirect

    elif user.groups.filter(name='technical').exists():
        return redirect('tech_admin:index')
    
    elif user.groups.filter(name='plataform').exists():
        return redirect('app:series') #provisional redirect

    else:
        return redirect('app:main')
    

# Vistas para el portal técnico (admin personalizado)

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .models import Profile

def tech_add_user_view(request):
    if request.method == 'POST':
        # Captura de datos de User
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password_again')
        
        # Captura de datos de Profile
        role_id = request.POST.get('role')
        profile_img = request.FILES.get('profile_image')

        # Validación simple de contraseña
        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect(request.path)

        try:
            # 1. Crear el objeto User
            user = User.objects.create_user(
                username=username, 
                email=email, 
                password=pass1,
                first_name=first_name,
                last_name=last_name
            )
            
            # 2. El Profile se crea solo por la Signal, así que lo recuperamos para actualizarlo
            profile = user.profile
            if role_id:
                group = Group.objects.get(id=role_id)
                profile.role = group
            if profile_img:
                profile.image = profile_img
            
            profile.save()
            messages.success(request, f"User {username} created successfully!")
            return redirect('tech_admin:index')
            
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect(request.path)

    # Para el GET, cargamos los grupos
    groups = Group.objects.all()
    return render(request, 'admin/tech_add_user.html', {'groups': groups})

def tech_edit_user_view(request, user_id):
    # Buscamos al usuario o lanzamos 404
    user_to_edit = get_object_or_404(User, id=user_id)
    groups = Group.objects.all()

    if request.method == 'POST':
        # 1. Actualizar datos básicos de User
        user_to_edit.username = request.POST.get('username')
        user_to_edit.first_name = request.POST.get('first_name')
        user_to_edit.last_name = request.POST.get('last_name')
        user_to_edit.email = request.POST.get('email')

        # 2. Gestión de contraseña (solo si se rellena)
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password_again')
        if pass1:
            if pass1 == pass2:
                user_to_edit.set_password(pass1)
            else:
                messages.error(request, "Las contraseñas no coinciden.")
                return redirect(request.path)

        # 3. Actualizar Profile (Rol e Imagen)
        role_id = request.POST.get('role')
        profile_img = request.FILES.get('profile_image')
        
        if role_id:
            user_to_edit.profile.role = Group.objects.get(id=role_id)
        
        if profile_img:
            user_to_edit.profile.image = profile_img
        
        try:
            user_to_edit.save()
            user_to_edit.profile.save()
            messages.success(request, f"Usuario {user_to_edit.username} actualizado correctamente.")
            return redirect('tech_admin:index')
        except Exception as e:
            messages.error(request, f"Error al guardar: {e}")

    return render(request, 'admin/tech_edit_user.html', {
        'user_to_edit': user_to_edit,
        'groups': groups
    })


def tech_delete_user(request, user_id):
    # Evitar que el usuario se borre a sí mismo por accidente
    if request.user.id == user_id:
        messages.error(request, "No puedes borrar tu propia cuenta desde aquí.")
        return redirect('tech_admin:index')

    user_to_delete = get_object_or_404(User, id=user_id)
    username = user_to_delete.username
    
    if request.method == 'POST':
        user_to_delete.delete()
        messages.success(request, f"Usuario {username} eliminado permanentemente.")
    
    return redirect('tech_admin:index')