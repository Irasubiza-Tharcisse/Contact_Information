from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Contact
# Create your views here.



# all contacts
@login_required
def all_contacts_view(request):
  user_active = request.user
  contacts = Contact.objects.filter(user=user_active)
  context={
    'username': user_active.username,
    'contacts': contacts,
  }
  if hasattr(user_active, 'is_staff') and user_active.is_staff:
    return render(request, 'contacts/all_contacts.html', {'contacts': Contact.objects.all()})
  else:
      return render(request, 'contacts/all_contacts_user.html', context)

# edit contact
@login_required
def contact_edit_view(request,contact_id):
  contact = get_object_or_404(Contact, id=contact_id)
  user_active = request.user
  context ={
    'username': user_active.username,
    'contact': contact,
  }
 
  if request.method == 'POST':
    contact.name = request.POST.get('name')
    contact.email = request.POST.get('email')
    contact.phone = request.POST.get('phone')
    contact.address = request.POST.get('address')
    contact.contact_type = request.POST.get('contact_type')
    contact.save()
    messages.success(request, f'Contact for {contact.name} was updated successfully')
    return redirect('all_contacts')
  if hasattr(user_active, 'is_staff') and user_active.is_staff:
    return render(request,'contacts/contact_edit.html',context)
  else:
    return render(request,'contacts/contact_edit_user.html',context)


# delete contact
@login_required
def delete_contact_view(request,contact_id):
  contact = get_object_or_404(Contact, id=contact_id)
  user_active = request.user
  context ={
    'username': user_active.username,
    'contact': contact,
  }
  if request.method == 'POST':
    
    contact.delete()
    messages.success(request, 'Contact deleted successfully!')
    return redirect('all_contacts')
  if hasattr(user_active, 'is_staff') and user_active.is_staff:
    return render(request,'contacts/delete_contact.html',context)
  else:
    return render(request,'contacts/delete_contact_user.html',context)
 

# new contact
@login_required
def new_contact_view(request):
  users = User.objects.all()
  user_active = request.user
  context ={
    'username': user_active.username,
    'users': users,
  }
  if request.method == 'POST':
    user_id = request.POST.get('user')
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    contact_type = request.POST.get('contact_type')
    contact = Contact(user_id=user_id,name=name,email=email,phone=phone,address=address,contact_type=contact_type)
    contact.save()
    messages.success(request, f'Contact for {contact.name} was created successfully')
    return redirect('all_contacts')
  if hasattr(user_active, 'is_staff') and user_active.is_staff:
    return render(request,'contacts/new_contact.html',context)
  else:
    return render(request,'contacts/new_contact_user.html',context)
 
  