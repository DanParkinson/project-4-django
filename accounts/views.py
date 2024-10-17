from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required # Users must be logged on to access this view
def account_details(request):
    return render(request, 'account/account_details.html')

class UserUpdateForm(forms.ModelForm):
    class meta:
        model = User 
        fields = ['username', 'email']


def account_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            message.success(request, "Your details have been updated.")
            return redirect('account_details')
        else:
            form = UserUpdateForm(instance=request.user)
    return render(request,  'account/account_update.html', {'form': form})
