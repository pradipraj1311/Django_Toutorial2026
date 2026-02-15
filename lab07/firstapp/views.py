from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'calc.html')

    def add(request):
        val1 = request.POST['num1']
            val2 = request.POST['num2']
                res = int(val1) + int(val2)
                    return render(request, 'result.html', {'result': res})
                    from django.shortcuts import render
                    from django.http import HttpResponse

                    # Create your views here.

                    def home(request):
                        return render(request, 'calc.html')

                        def add(request):
                            val1 = request.POST['num1']
                                val2 = request.POST['num2']
                                    res = int(val1) + int(val2)
                                        return render(request, 'result.html', {'result': res})
                                        
                    # View for the Django Form (Lab 7 Part 3)
                    def my_form_view(request):
                        if request.method == 'POST':
                                form = MyForm(request.POST)
                                        if form.is_valid():
                                                    # Process valid form data here if needed
                                                                pass 
                                                                    else:
                                                                            form = MyForm()
                                                                                
                                                                                    return render(request, 'my_template.html', {'form': form})
