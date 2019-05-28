from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

races = {
    'White',
    'Black',
    'Hispanic',
    'Asian',
}

heights = {
    'Short',
    'Average',
    'Tall',
}

builds = {
    'Thin',
    'Average',
    'Solid',
    'Large',
}

incomes = {
    'Low',
    'Medium',
    'High',
}

educations = {
    'High school degree',
    'College degree',
    'Graduate degree',
}

politicals = {
    'Liberal',
    'Conservative',
}

@app.route('/', methods = ['GET', 'POST'])
def index():

    a_attributes = {
        'Race': 'white',
        'Height': 'average',
        'Build': 'average',
        'Income': 'low',
        'Education': 'college',
        'Political orientation': 'liberal',
    }

    b_attributes = {
        'Race': 'black',
        'Height': 'short',
        'Build': 'solid',
        'Income': 'high',
        'Education': 'high school',
        'Political orientation': 'conservative',
    }

    dates = {'a':'john', 'b':'jake'}

    if request.method == 'POST':
        if request.form['date'] == dates['a']:
            return render_template('index.html', dates=dates, a_attributes=a_attributes, b_attributes=b_attributes)
        elif request.form['date'] == dates['b']:
            return render_template('index.html', dates=dates, a_attributes=a_attributes, b_attributes=b_attributes)
        else:
            pass

    elif request.method == 'GET':
        return render_template('index.html', dates=dates, a_attributes=a_attributes, b_attributes=b_attributes)

if __name__ == "__main__":
    app.run()
