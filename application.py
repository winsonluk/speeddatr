from ast import literal_eval
from copy import deepcopy
from flask import Flask
from flask import render_template
from flask import request
from heapq import *
from random import Random, randint, shuffle

application = Flask(__name__)

characteristics = {
    'Race': [
        'White',
        'Black',
        'Hispanic',
        'Asian',
    ],
    'Height': [
        'Short',
        'Tall',
    ],
    'Build': [
        'Thin',
        'Heavy',
    ],
    'Income': [
        'Low',
        'High',
    ],
    'Education': [
        'High school degree',
        'Graduate degree',
    ],
    'Political orientation': [
        'Democrat',
        'Republican',
    ],
}

master_stats = {
    'Race': {
        'White': 0,
        'Black': 0,
        'Hispanic': 0,
        'Asian': 0,
    },
    'Height': {
        'Short': 0,
        'Tall': 0,
    },
    'Build': {
        'Thin': 0,
        'Heavy': 0,
    },
    'Income': {
        'Low': 0,
        'High': 0,
    },
    'Education': {
        'High school degree': 0,
        'Graduate degree': 0,
    },
    'Political orientation': {
        'Democrat': 0,
        'Republican': 0,
    },
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

def show_results(stats):

    print(stats)

    strongest_biases = []
    nonbiased = set()

    for attr in stats:
        nonbiased.add(attr.lower())
        for char in stats[attr]:

            if attr == 'Race':
                if stats[attr][char] > 0:
                    heappush(strongest_biases, (-3 * stats[attr][char], (attr, char, 'positive')))
                else:
                    heappush(strongest_biases, (-3 * abs(stats[attr][char]), (attr, char, 'negative')))
            else:
                if stats[attr][char] > 0:
                    heappush(strongest_biases, (-1 * stats[attr][char], (attr, char, 'positive')))
                else:
                    heappush(strongest_biases, (-1 * abs(stats[attr][char]), (attr, char, 'negative')))

    attrs = []
    chars = []
    direction_nouns = []
    direction_verbs = []
    print(strongest_biases)

    while len(attrs) < 3:
        try:
            _, biases = heappop(strongest_biases)
            print(biases)
            if biases[0].lower() in attrs:
                continue
            attrs.append(biases[0].lower())
            chars.append(biases[1])
            direction = biases[2]
            if direction == 'positive':
                direction_nouns.append('positive')
                direction_verbs.append('towards')
            elif direction == 'negative':
                direction_nouns.append('negative')
                direction_verbs.append('against')
        except:
            return render_template('index.html')

    for attr in attrs:
        nonbiased.remove(attr)

    return render_template(
            'results.html',
            attr=attrs,
            direction_noun=direction_nouns,
            direction_verb=direction_verbs,
            char=chars,
            nonbiased=nonbiased,
    )

@application.route('/', methods = ['GET', 'POST'])
def index():

    if request.method == 'POST':

        curr_comparison = int(request.form['curr_comparison'])

        seed = randint(0, 99)
        stats = deepcopy(master_stats)
        if curr_comparison > 0:
            seed = request.form['seed']
            stats = literal_eval(request.form['stats'])

        if curr_comparison < 20:

            combinations = deepcopy(master_combinations)
            Random(seed).shuffle(combinations)

            a_attributes = {}
            b_attributes = {}

            attrs = combinations[curr_comparison]

            for attr in attrs:
                attr_len = len(characteristics[attr])
                a_attributes[attr] = characteristics[attr][randint(0, attr_len - 1)]
                b_attributes[attr] = characteristics[attr][randint(0, attr_len - 1)]

            names = deepcopy(master_names)
            shuffle(names)
            name_1 = names.pop()
            name_2 = names.pop()
            dates = {'a': name_1, 'b': name_2}

            if 'date' in request.form:

                if request.form['date'] == request.form['name_1']:
                    chosen_attributes = literal_eval(request.form['a_attributes'])
                    rejected_attributes = literal_eval(request.form['b_attributes'])
                elif request.form['date'] == request.form['name_2']:
                    chosen_attributes = literal_eval(request.form['b_attributes'])
                    rejected_attributes = literal_eval(request.form['a_attributes'])
                for attr in chosen_attributes:
                    stats[attr][chosen_attributes[attr]] += 1
                for attr in rejected_attributes:
                    stats[attr][rejected_attributes[attr]] -= 1

                curr_comparison += 1

            else:
                curr_comparison = 1

            return render_template(
                    'compare.html',
                    dates=dates,
                    name_1=name_1,
                    name_2=name_2,
                    a_attributes=a_attributes,
                    b_attributes=b_attributes,
                    curr_comparison=curr_comparison,
                    seed=seed,
                    stats=stats,
            )

        else:
            if request.form['date'] == request.form['name_1']:
                chosen_attributes = literal_eval(request.form['a_attributes'])
                rejected_attributes = literal_eval(request.form['b_attributes'])
            elif request.form['date'] == request.form['name_2']:
                chosen_attributes = literal_eval(request.form['b_attributes'])
                rejected_attributes = literal_eval(request.form['a_attributes'])
            for attr in chosen_attributes:
                stats[attr][chosen_attributes[attr]] += 1
            for attr in rejected_attributes:
                stats[attr][rejected_attributes[attr]] -= 1
            return show_results(stats)

    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == "__main__":
    application.run()
