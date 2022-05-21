from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': 'Li Pon', 'place': 'Mars'}
    return render(request,'index.html', params)


def analyze(request):
    # Get the text
    text_area_text = request.POST.get('text', 'default')
    # Check the iteem on or off
    punctuation_check = request.POST.get('punctuation', 'off')
    full_capital_check = request.POST.get('full_capital', 'off')
    new_line_remover_check = request.POST.get('new_line_remover', 'off')
    extra_space_check = request.POST.get('extraspace', 'off')
    charecter_counter_check = request.POST.get('char_counter', 'off')
    # Analyze the text
    if punctuation_check == 'on':
        punctuation_marks = '''.,?;!:'()[]"_-/@#$%^&*}{~'''
        analyzed = ""
        for char in text_area_text:
            if char not in punctuation_marks:
                analyzed += char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed,}
        text_area_text = analyzed
        # return render(request, 'analyze.html', params)
    if full_capital_check == 'on':
        analyzed = ""
        for char in text_area_text:
            analyzed += char.upper()
        params = {'purpose': 'Full Capital', 'analyzed_text': analyzed}
        text_area_text = analyzed
        # return render(request, 'analyze.html', params)
    if new_line_remover_check == 'on':
        analyzed = ""
        for char in text_area_text:
            if char != "\n" and char !="\r":
                analyzed += char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        text_area_text = analyzed
        # return render(request, 'analyze.html', params)
    if extra_space_check == 'on':
        analyzed = ""
        for index, char in enumerate(text_area_text):
            if not (text_area_text[index] == " " and text_area_text[index+1] == " "):
                analyzed += char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        text_area_text = analyzed
        # return render(request, 'analyze.html', params)
    if (punctuation_check != 'on' and full_capital_check != 'on' and new_line_remover_check != 'on' and extra_space_check != 'on' and charecter_counter_check != 'on'):
        return HttpResponse("Please select an option")
    
    if charecter_counter_check == 'on':
        count_charecter = 0
        for char in text_area_text:
            if char != " ":
                count_charecter += 1
        params = {'purpose': 'Charecter Counter', 'count_charecter': count_charecter, 'analyzed_text': analyzed}

    return render(request, 'analyze.html', params)
