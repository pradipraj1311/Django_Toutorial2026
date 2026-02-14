from django.shortcuts import render
from django.http import HttpResponse

# View to render the initial calculation form
def home(request):
    [span_5](start_span)return render(request, 'calc.html') #[span_5](end_span)

    # View to process the addition logic
    def add(request):
        [span_6](start_span)val1 = request.POST['num1'] #[span_6](end_span)
            [span_7](start_span)val2 = request.POST['num2'] #[span_7](end_span)
                [span_8](start_span)res = int(val1) + int(val2) #[span_8](end_span)
                    
                        [span_9](start_span)return render(request, 'result.html', {'result': res}) #[span_9](end_span)
                        