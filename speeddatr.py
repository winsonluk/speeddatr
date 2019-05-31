from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

characteristics = {

    'races': [
        'White',
        'Black',
        'Hispanic',
        'Asian',
    ],

    'heights': [
        'Short',
        'Average',
        'Tall',
    ],

    'builds': [
        'Thin',
        'Average',
        'Solid',
        'Large',
    ],

    'incomes': [
        'Low',
        'Medium',
        'High',
    ],

    'educations': [
        'High school degree',
        'College degree',
        'Graduate degree',
    ],

    'politicals': [
        'Liberal',
        'Conservative',
    ],
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

        curr_comparison = int(request.form['curr_comparison'])

        if curr_comparison < 20:

            if request.form['date'] == dates['a']:
                curr_comparison += 1
                return render_template('compare.html',
                        dates=dates,
                        a_attributes=a_attributes,
                        b_attributes=b_attributes,
                        curr_comparison=curr_comparison
                )

            elif request.form['date'] == dates['b']:
                curr_comparison += 1
                return render_template('compare.html',
                        dates=dates,
                        a_attributes=a_attributes,
                        b_attributes=b_attributes,
                        curr_comparison=curr_comparison
                )

            else:
                curr_comparison += 1
                return render_template('compare.html',
                        dates=dates,
                        a_attributes=a_attributes,
                        b_attributes=b_attributes,
                        curr_comparison=curr_comparison
                )

        else:
            return render_template('results.html')

    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == "__main__":
    app.run()
