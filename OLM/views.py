from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def encrypt(request):
    input_text = request.POST.get('input','default')
    punctuations ='''!()-[]{};:'"\,<>./?@#$%^&8_~'''
    analyzed =""
    for char in input_text:
        if char not in punctuations:
            analyzed = analyzed + char

    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}

    analyzed = analyzed.upper()
    cipher = ''
    for letter in analyzed:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    params = {'analyzed_text': cipher}
    return render(request,'index.html',params)