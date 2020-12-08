from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .forms import Linear_generator
import math, random


def main(request):
    return render(request, 'generators_site/main.html')


def Linear_Congruential_generator(request):
    try:
        m = int(request.POST.get('m'))
        a = int(request.POST.get('a'))
        c = int(request.POST.get('c'))
        size = int(request.POST.get('size'))
        submitbutton = request.POST.get('Submit')
        iterlist = [0]
        iterlist[0] = math.ceil(random.randint(1, 10000))
        for i in range(1, size + 1):
            iterlist.append(math.ceil(math.fmod((a * iterlist[i - 1] + c), m)))
        freq = [0]*10
        for n in iterlist:
            while True:
                 try:
                     freq[(n-1)//((m//10))]+=1
                     break
                 except IndexError:
                     freq[9]+=1
                     break
        for i in range(10):
            freq[i] = round(freq[i]/size, 4)
        context = {'m': m, 'a': a, 'c': c, 'size': size, 'submitbutton': submitbutton, 'iterlist': iterlist[1:int(size)+1],
                   'f0' : freq[0], 'f1' : freq[1], 'f2' : freq[2], 'f3' : freq[3], 'f4' : freq[4], 'f5' : freq[5], 'f6' : freq[6],
                   'f7' :freq[7], 'f8' : freq[8], 'f9' : freq[9]}
        return render(request, 'generators_site/Linear_Congruential_generator.html', context)
    except TypeError:
        return render(request, 'generators_site/Linear_Congruential_generator.html')



def Square_Congruential_generator(request):
    try:
        m = int(request.POST.get('m'))
        a = int(request.POST.get('a'))
        c = int(request.POST.get('c'))
        d = int(request.POST.get('d'))
        size = int(request.POST.get('size'))
        submitbutton = request.POST.get('Submit')
        iterlist = [0]
        iterlist[0] = math.ceil(random.randint(1, 4809))
        for i in range(1, size + 1):
            iterlist.append(math.ceil(math.fmod((d * (iterlist[i - 1] ** 2) + a * iterlist[i - 1] + c), m)))
        freq = [0]*10
        for n in iterlist:
            while True:
                 try:
                     freq[(n-1)//((m//10))]+=1
                     break
                 except IndexError:
                     freq[9]+=1
                     break
        for i in range(10):
            freq[i] = round(freq[i]/size, 4)
        context = {'m': m, 'a': a, 'c': c, 'd':d, 'size': size, 'submitbutton': submitbutton, 'iterlist': iterlist[1:int(size)+1],
                   'f0': freq[0], 'f1': freq[1], 'f2': freq[2], 'f3': freq[3], 'f4': freq[4], 'f5': freq[5],
                   'f6': freq[6],'f7': freq[7], 'f8': freq[8], 'f9': freq[9]}
        return render(request, 'generators_site/Square_Congruential_generator.html', context)
    except:
        return render(request, 'generators_site/Square_Congruential_generator.html')




def Fibonacci_generator(request):
    try:
        m = int(request.POST.get('size'))
        size = int(request.POST.get('size'))
        submitbutton = request.POST.get('Submit')
        iterlist = []
        iterlist.append(math.ceil(random.randint(1, 50000)))
        iterlist.append(math.ceil(random.randint(1, 50000)))
        for i in range(2, size + 2):
            iterlist.append(math.ceil(math.fmod((iterlist[i - 1] + iterlist[i - 2]), m)))
        freq = [0]*10
        for n in iterlist:
            while True:
                try:
                    freq[(n - 1) // ((m // 10))] += 1
                    break
                except IndexError:
                    freq[9] += 1
                    break
        for i in range(10):
            freq[i] = round(freq[i] / size, 4)
        context = {'m': m, 'size': size, 'submitbutton': submitbutton, 'iterlist': iterlist[2:size+1],
                   'f0': freq[0], 'f1': freq[1], 'f2': freq[2], 'f3': freq[3], 'f4': freq[4], 'f5': freq[5],
                   'f6': freq[6], 'f7': freq[7], 'f8': freq[8], 'f9': freq[9]}
        return render(request, 'generators_site/Fibonacci_generator.html', context)
    except:
        return render(request, 'generators_site/Fibonacci_generator.html')


def Reverse_Congruential_generator(request):
    try:
        m = int(request.POST.get('m'))
        a = int(request.POST.get('a'))
        c = int(request.POST.get('c'))
        size = int(request.POST.get('size'))
        submitbutton = request.POST.get('Submit')
        def rev(a, m):
            i = 1
            while True:
                if (a * i) % m == 1:
                    return i
                i += 1
        iterlist = [0]
        iterlist[0] = math.ceil(random.randint(1, 50003))
        for i in range(1, size + 1):
            if math.gcd(iterlist[i - 1], m) != 1:
                return False
            iterlist.append(math.ceil(math.fmod((a * rev(iterlist[i - 1], m) + c), m)))
        freq = [0]*10
        for n in iterlist:
            while True:
                try:
                    freq[(n - 1) // ((m // 10))] += 1
                    break
                except IndexError:
                    freq[9] += 1
                    break
        for i in range(10):
            freq[i] = round(freq[i] / size, 4)
        context = {'m': m, 'size': size, 'submitbutton': submitbutton, 'iterlist': iterlist[2:size+1],
                   'f0': freq[0], 'f1': freq[1], 'f2': freq[2], 'f3': freq[3], 'f4': freq[4], 'f5': freq[5],
                   'f6': freq[6], 'f7': freq[7], 'f8': freq[8], 'f9': freq[9]}
        return render(request, 'generators_site/Reverse_Congruential_generator.html', context)
    except:
        return render(request, 'generators_site/Reverse_Congruential_generator.html')



def Associative_generator(request):
    try:
        m = int(request.POST.get('m'))
        a = int(request.POST.get('a'))
        size = int(request.POST.get('size'))
        submitbutton = request.POST.get('Submit')
        iterlist = []
        for i in range(size):
            iterlist.append(math.ceil(abs(math.fmod((random.randint(1, m) - random.randint(1, m)), m))))
        freq = [0]*10
        for n in iterlist:
            while True:
                try:
                    freq[(n - 1) // ((m // 10))] += 1
                    break
                except IndexError:
                    freq[9] += 1
                    break
        for i in range(10):
            freq[i] = round(freq[i] / size, 4)
        context = {'size': size, 'submitbutton': submitbutton, 'iterlist': iterlist[2:size+1],
                   'f0': freq[0], 'f1': freq[1], 'f2': freq[2], 'f3': freq[3], 'f4': freq[4], 'f5': freq[5],
                   'f6': freq[6], 'f7': freq[7], 'f8': freq[8], 'f9': freq[9]}
        return render(request, 'generators_site/Assosiative_generator.html', context)
    except:
        return render(request, 'generators_site/Assosiative_generator.html')

def Three_sigma_generator(request):
    try:
        size = int(request.POST.get('size'))
        submitbutton = request.POST.get('Submit')
        sum = 0
        iterlist = []
        for i in range(size):
            for i in range(12):
                sum += random.random()
            iterlist.append(sum - 6)
            sum = 0
        freq = [0]*4
        for n in iterlist:
            if n <-1.5:
                freq[0] +=1
            elif n < 0:
                freq[1] +=1
            elif n< 1.5:
                freq[2] +=1
            else:
                freq[3] +=1
        for i in range(4):
            freq[i] = round(freq[i] / size, 4)
        context = {'size': size, 'submitbutton': submitbutton, 'iterlist': iterlist[2:size + 1],
                           'f0': freq[0], 'f1': freq[1], 'f2': freq[2], 'f3': freq[3]}
        return render(request, 'generators_site/Three_sigma_generator.html', context)
    except:
        return render(request, 'generators_site/Three_sigma_generator.html')


def Poliar_Cords_generator(request):
    try:
        size = int(request.POST.get('size'))
        submitbutton = request.POST.get('Submit')
        iterlist = []
        for i in range(size // 2):
            while True:
                u1, u2 = random.random(), random.random()
                v1 = (2 * u1) - 1
                v2 = (2 * u2) - 1
                s = (v1 * v1) + (v2 * v2)
                if s >= 1:
                    continue
                break
            iterlist.append(v1 * (math.sqrt((-2 * math.log(s)) / s))+5)
            iterlist.append(v2 * (math.sqrt((-2 * math.log(s)) / s))+5)
        freq = [0] * 10
        for n in iterlist:
            while True:
                try:
                    freq[int(n)] += 1
                    break
                except IndexError:
                    freq[9] += 1
                    break
        for i in range(10):
            freq[i] = round(freq[i] / size, 4)
        context = {'size': size, 'submitbutton': submitbutton, 'iterlist': iterlist[2:size+1],
                   'f0': freq[0], 'f1': freq[1], 'f2': freq[2], 'f3': freq[3], 'f4': freq[4], 'f5': freq[5],
                   'f6': freq[6], 'f7': freq[7], 'f8': freq[8], 'f9': freq[9]}
        return render(request, 'generators_site/Poliar_Cords_generator.html', context)
    except:
        return render(request, 'generators_site/Poliar_Cords_generator.html',)


def Relative_generator(request):
    try:
        size = int(request.POST.get('size'))
        submitbutton = request.POST.get('Submit')
        iterlist = []
        for i in range(size):
            while True:
                u, v = random.random(), random.random()
                x = math.sqrt(8 / math.e) * ((v - 0.5) / u)
                if x * x > -4 * math.log(u):
                    continue
                break
            iterlist.append(x+5)
        freq = [0] * 10
        for n in iterlist:
            while True:
                try:
                    freq[int(n)] += 1
                    break
                except IndexError:
                    freq[9] += 1
                    break
        for i in range(10):
            freq[i] = round(freq[i] / size, 4)
        context = {'size': size, 'submitbutton': submitbutton, 'iterlist': iterlist[2:size+1],
                   'f0': freq[0], 'f1': freq[1], 'f2': freq[2], 'f3': freq[3], 'f4': freq[4], 'f5': freq[5],
                   'f6': freq[6], 'f7': freq[7], 'f8': freq[8], 'f9': freq[9]}
        return render(request, 'generators_site/Relative_generator.html', context)
    except:
        return render(request, 'generators_site/Relative_generator.html',)

def Logarithm_generator(request):
    try:
        nu = float(request.POST.get('nu'))
        size = int(request.POST.get('size'))
        submitbutton = request.POST.get('Submit')
        iterlist = []
        for i in range(size):
            x = -nu * math.log(random.random())
            iterlist.append(round(x, 4))
        freq = [0] * 10
        for k in iterlist:
            if k >3:
                freq[4]+=1
            elif k >2:
                freq[3]+=1
            elif k >1:
                freq[2]+=1
            elif k >0.5:
                freq[1]+=1
            else:
                freq[0]+=1
        for i in range(10):
            freq[i] = round(freq[i] / size, 4)
        context = {'size': size, 'submitbutton': submitbutton, 'iterlist': iterlist[2:size+1],
                   'f0': freq[0], 'f1': freq[1], 'f2': freq[2], 'f3': freq[3], 'f4': freq[4]}
        return render(request, 'generators_site/Logarithm_generator.html', context)
    except:
        return render(request, 'generators_site/Logarithm_generator.html',)


def Arence_generator(request):
    try:
        a = int(request.POST.get('a'))
        size = int(request.POST.get('size'))
        submitbutton = request.POST.get('Submit')
        iterlist = []
        for i in range(size):
            while True:
                y = math.tan(math.pi * random.random())
                x = math.sqrt(2 * a - 1) + y + a - 1
                v = random.random()
                if x > 0 and v > (x + y ** 2) * math.e * ((a - 1) * math.log(x / (a - 1)) - math.sqrt(2 * a - 1) + y):
                    break
            iterlist.append(round(x, 4))
        freq = [0]*5
        for k in iterlist:
            if k<0.5:
                freq[0]+=1
            elif k <1:
                freq[1] +=1
            elif k <2:
                freq[2]+=1
            elif k <3:
                freq[3]+=1
            else:
                freq[4]+=1
        for i in range(5):
            freq[i] = round(freq[i] / size, 4)
        context = {'size': size, 'submitbutton': submitbutton, 'iterlist': iterlist[:],
                   'f0': freq[0], 'f1': freq[1], 'f2': freq[2], 'f3': freq[3], 'f4': freq[4]}
        return render(request, 'generators_site/Arence_generator.html', context)
    except:
        return render(request, 'generators_site/Arence_generator.html')
