from copy import deepcopy
from flask import Flask
from flask import render_template
from flask import request
from random import Random, randint, shuffle

app = Flask(__name__)

characteristics = {
    'Race': [
        'White',
        'Black',
        'Hispanic',
        'Asian',
    ],
    'Height': [
        'Short',
        'Average',
        'Tall',
    ],
    'Build': [
        'Thin',
        'Average',
        'Solid',
        'Large',
    ],
    'Income': [
        'Low',
        'Medium',
        'High',
    ],
    'Education': [
        'High school degree',
        'College degree',
        'Graduate degree',
    ],
    'Political orientation': [
        'Liberal',
        'Conservative',
    ],
}

master_combinations = [
    ['Race', 'Height', 'Build'],
    ['Race', 'Height', 'Income'],
    ['Race', 'Height', 'Education'],
    ['Race', 'Height', 'Political orientation'],
    ['Race', 'Build', 'Income'],
    ['Race', 'Build', 'Education'],
    ['Race', 'Build', 'Political orientation'],
    ['Race', 'Income', 'Education'],
    ['Race', 'Income', 'Political orientation'],
    ['Race', 'Education', 'Political orientation'],
    ['Height', 'Build', 'Income'],
    ['Height', 'Build', 'Education'],
    ['Height', 'Build', 'Political orientation'],
    ['Height', 'Income', 'Education'],
    ['Height', 'Income', 'Political orientation'],
    ['Height', 'Education', 'Political orientation'],
    ['Build', 'Income', 'Education'],
    ['Build', 'Income', 'Political orientation'],
    ['Build', 'Education', 'Political orientation'],
    ['Income', 'Education', 'Political orientation'],
]

master_names = [
    'Dana',
    'Jesse',
    'Skyler',
    'Riley',
    'Sidney',
    'Robin',
    'Harper',
    'Dakota',
    'Morgan',
    'Madison',
    'Perry',
    'Jaidyn',
    'Jules',
    'Jamie',
    'Jackie',
    'Peyton',
    'Ridley',
    'Casey',
    'Alex',
    'Taylor',
]

@app.route('/', methods = ['GET', 'POST'])
def index():

    if request.method == 'POST':

        curr_comparison = int(request.form['curr_comparison'])

        if curr_comparison < 20:

            seed = randint(0, 20)
            if curr_comparison > 0:
                seed = request.form['seed']

            combinations = deepcopy(master_combinations)
            Random(seed).shuffle(combinations)

            a_attributes = {}
            b_attributes = {}

            attrs = combinations[curr_comparison]
            shuffle(attrs)

            for attr in attrs:
                attr_len = len(characteristics[attr])
                a_attributes[attr] = characteristics[attr][randint(0, attr_len - 1)]
                b_attributes[attr] = characteristics[attr][randint(0, attr_len - 1)]

            names = deepcopy(master_names)
            idx = randint(0,len(names) - 1)
            name_1 = names.pop(idx)
            name_2 = names[randint(0, len(names) - 1)]
            dates = {'a': name_1, 'b': name_2}

            if request.form['date'] == request.form['name_1']:
                print(request.form['a_attributes'])
                curr_comparison += 1
                return render_template('compare.html',
                        dates=dates,
                        name_1=name_1,
                        name_2=name_2,
                        a_attributes=a_attributes,
                        b_attributes=b_attributes,
                        curr_comparison=curr_comparison,
                        seed=seed,
                )

            elif request.form['date'] == request.form['name_2']:
                print(request.form['b_attributes'])
                curr_comparison += 1
                return render_template('compare.html',
                        dates=dates,
                        name_1=name_1,
                        name_2=name_2,
                        a_attributes=a_attributes,
                        b_attributes=b_attributes,
                        curr_comparison=curr_comparison,
                        seed=seed,
                )

            else:
                curr_comparison = 1
                return render_template('compare.html',
                        dates=dates,
                        name_1=name_1,
                        name_2=name_2,
                        a_attributes=a_attributes,
                        b_attributes=b_attributes,
                        curr_comparison=curr_comparison,
                        seed=seed,
                )

        else:
            if request.form['date'] == request.form['name_1']:
                print(request.form['a_attributes'])
            elif request.form['date'] == request.form['name_2']:
                print(request.form['b_attributes'])
            return render_template('results.html')

    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == "__main__":
    app.run()
