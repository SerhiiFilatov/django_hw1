from django.http import HttpRequest
from django.http import HttpResponse


def ex_home(request: HttpRequest)->HttpResponse:
    return HttpResponse('<h3>Hello!!!</h>')

def ex_greeting(request: HttpRequest, name: str)->HttpResponse:
    return HttpResponse(f'<h1>Helo, {name}</h>')

def ex_progression(request: HttpRequest, start: int, count: int, step: int)->HttpResponse:
    num_start = start
    f = ''
    for i in range(count):
        num_start += step
        f += f' {str(num_start)}'
    return HttpResponse(f)

def ex_fib (request: HttpRequest, x: int):
    def fib(n):
        if n == 1 or n == 2:
            return 1
        return fib(n - 1) + fib(n - 2)
    return HttpResponse(fib(x))