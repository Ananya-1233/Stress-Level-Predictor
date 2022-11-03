from django.shortcuts import render

from joblib import load
model = load('./savedModel/model.joblib')

def prediction(request):
    if request.method == 'POST':
        sr = request.POST['sr']
        rr = request.POST['rr']
        bt = request.POST['bt']
        lm = request.POST['lm']
        bo = request.POST['bo']
        em = request.POST['em']
        sh = request.POST['sh']
        hr = request.POST['hr']
        

        sr = float('0' + sr)
        rr = float('0' + rr)
        bt = float('0' + bt)
        lm = float('0' + lm)
        bo = float('0' + bo)
        em = float('0' + em)
        sh = float('0' + sh)
        hr = float('0' + hr)



        y_pred = model.predict([[sr,rr,bt,lm,bo,em,sh,hr]])
        if y_pred[0] == 0:
            y_pred = 'Great'
        elif y_pred[0] == 1:
            y_pred = 'Needs improvement'
        elif y_pred[0] == 2:
            y_pred = 'Bad'
        return render(request, 'main.html', {'result' : y_pred})
    return render(request, 'main.html')