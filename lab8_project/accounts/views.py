from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def secret_page(request):
    # Only logged in users see this
        ...
        
# Create your views here.
from django.shortcuts import render
from .forms import ContactForm  # Import the form we just created

def contact_view(request):
    if request.method == 'POST':
            # If the user submitted the form
                    form = ContactForm(request.POST)
                            if form.is_valid():
                                        # In a real app, you would save data here
                                                    # For now, we just print "Success" to the terminal
                                                                print("VALIDATION SUCCESS!")
                                                                    else:
                                                                            # If the user is just visiting the page (GET request)
                                                                                    form = ContactForm()

                                                                                        return render(request, 'contact.html', {'form': form})
                                                                                        