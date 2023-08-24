'''from flask import Flask, render_template_string
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Hardcoded training and test data
training_data = [
    [25, 1, 110, 0],
    [30, 0, 95, 0],
    [40, 2, 85, 1],
    [55, 1, 105, 0],
    [60, 0, 125, 1],
    [70, 0, 80, 1],
    [35, 2, 130, 1],
    [45, 1, 100, 0],
    [50, 2, 115, 0]
]

test_data = [
    [28, 1, 108, 0],
    [32, 0, 90, 0],
    [42, 2, 128, 1],
    [58, 1, 122, 1]
]

@app.route('/')
def index():
    # Splitting data into features and labels
    X_train = [x[:-1] for x in training_data]
    y_train = [x[-1] for x in training_data]

    X_test = [x[:-1] for x in test_data]

    # Training a RandomForest classifier
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # Predicting on test data
    y_pred = clf.predict(X_test)

    results = []
    for data, prediction in zip(test_data, y_pred):
        results.append({
            "Age": data[0],
            "Activity Level": data[1],
            "Blood Pressure": data[2],
            "Prediction": 'Unusual' if prediction else 'Normal'
        })

    # Rendering the results to a web page
    html_template = """
    <h1>Blood Pressure Test Results</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Age</th>
                <th>Activity Level</th>
                <th>Blood Pressure</th>
                <th>Prediction</th>
            </tr>
        </thead>
        <tbody>
            {% for result in results %}
            <tr>
                <td>{{ result["Age"] }}</td>
                <td>{{ result["Activity Level"] }}</td>
                <td>{{ result["Blood Pressure"] }}</td>
                <td>{{ result["Prediction"] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    """

    return render_template_string(html_template, results=results)


if __name__ == '__main__':
    app.run(debug=True)
'''

'''
from flask import Flask, render_template_string, request
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Hardcoded training and test data
training_data = [
    [25, 1, 110, 0],
    [30, 0, 95, 0],
    [40, 2, 85, 1],
    [55, 1, 105, 0],
    [60, 0, 125, 1],
    [70, 0, 80, 1],
    [35, 2, 130, 1],
    [45, 1, 100, 0],
    [50, 2, 115, 0]
]

test_data = [
    [28, 1, 108, 0],
    [32, 0, 90, 0],
    [42, 2, 128, 1],
    [58, 1, 122, 1]
]

@app.route('/', methods=['GET', 'POST'])
def index():
    # Splitting data into features and labels
    X_train = [x[:-1] for x in training_data]
    y_train = [x[-1] for x in training_data]
    X_test = [x[:-1] for x in test_data]
    
    # Training a RandomForest classifier
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # Predicting on test data
    y_pred = clf.predict(X_test)

    results = []
    for data, prediction in zip(test_data, y_pred):
        results.append({
            "Age": data[0],
            "Activity Level": data[1],
            "Blood Pressure": data[2],
            "Prediction": 'Unusual' if prediction else 'Normal'
        })

    user_result = None
    if request.method == 'POST':
        # Get data from the form
        age = int(request.form['age'])
        activity_level = int(request.form['activity_level'])
        bp = int(request.form['bp'])
        
        # Make prediction
        user_pred = clf.predict([[age, activity_level, bp]])
        user_result = {
            "Age": age,
            "Activity Level": activity_level,
            "Blood Pressure": bp,
            "Prediction": 'Unusual' if user_pred[0] else 'Normal'
        }
        results.append(user_result)

    # Rendering the results to a web page
    html_template = """
    <h1>Blood Pressure Test Results</h1>
    <form method="post">
        Age: <input type="number" name="age"><br>
        Activity Level (0, 1, or 2): <input type="number" name="activity_level" min="0" max="2"><br>
        Blood Pressure: <input type="number" name="bp"><br>
        <input type="submit" value="Predict">
    </form>
    <table border="1">
        <thead>
            <tr>
                <th>Age</th>
                <th>Activity Level</th>
                <th>Blood Pressure</th>
                <th>Prediction</th>
            </tr>
        </thead>
        <tbody>
            {% for result in results %}
            <tr>
                <td>{{ result["Age"] }}</td>
                <td>{{ result["Activity Level"] }}</td>
                <td>{{ result["Blood Pressure"] }}</td>
                <td>{{ result["Prediction"] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    """

    return render_template_string(html_template, results=results)

if __name__ == '__main__':
    app.run(debug=True)
'''

from flask import Flask, render_template_string, request
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Hardcoded training data
training_data = [
    [25, 1, 110, 0],
    [30, 0, 95, 0],
    [40, 2, 85, 1],
    [55, 1, 105, 0],
    [60, 0, 125, 1],
    [70, 0, 80, 1],
    [35, 2, 130, 1],
    [45, 1, 100, 0],
    [50, 2, 115, 0]
]

@app.route('/', methods=['GET', 'POST'])
def index():
    # Splitting data into features and labels
    X_train = [x[:-1] for x in training_data]
    y_train = [x[-1] for x in training_data]
    
    # Training a RandomForest classifier
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    user_result = None
    if request.method == 'POST':
        # Get data from the form
        age = int(request.form['age'])
        activity_level = int(request.form['activity_level'])
        bp = int(request.form['bp'])
        
        # Make prediction
        user_pred = clf.predict([[age, activity_level, bp]])
        user_result = {
            "Age": age,
            "Activity Level": activity_level,
            "Blood Pressure(in mmHg)": bp,  # Change made here
            "Prediction": 'Unusual' if user_pred[0] else 'Normal'
        }

    html_template = """
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: lightpink;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        form {
            display: grid;
            gap: 10px;
        }
        h1, h2 {
            text-align: center;
        }
    </style>
    <div class="container">
        <h1>Blood Pressure Test</h1>
        <form method="post">
            Age: <input type="number" name="age">
            Activity Level (0, 1, or 2): <input type="number" name="activity_level" min="0" max="2">
            Blood Pressure(in mmHg): <input type="number" name="bp">  <!-- Change made here -->
            <input type="submit" value="Predict">
        </form>
        {% if user_result %}
        <h2>Your Result:</h2>
        <p>Age: {{ user_result["Age"] }}</p>
        <p>Activity Level: {{ user_result["Activity Level"] }}</p>
        <p>Blood Pressure(in mmHg): {{ user_result["Blood Pressure(in mmHg)"] }}</p>  <!-- Change made here -->
        <p>Prediction: {{ user_result["Prediction"] }}</p>
        {% endif %}
    </div>
    """

    return render_template_string(html_template, user_result=user_result)

if __name__ == '__main__':
    app.run(debug=True)
