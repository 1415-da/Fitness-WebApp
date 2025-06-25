from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Static data for recommendation page
        experience_level = 'Intermediate'
        experience_years = 3
        plan = {
            'Monday': ['Push-ups', 'Squats', 'Running'],
            'Tuesday': ['Pull-ups', 'Lunges', 'Plank'],
            'Wednesday': ['Rest'],
            'Thursday': ['Push-ups', 'Squats', 'Deadlifts'],
            'Friday': ['Pull-ups', 'Lunges', 'Bicycle Crunches'],
            'Saturday': ['Cardio'],
            'Sunday': ['Rest']
        }
        nutrition = "Eat lean proteins, vegetables, and healthy fats for balanced nutrition."
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        progress_data = [5, 7, 2, 8, 6, 9, 3]  # Example static progress data

        return render_template('recommendation.html',
                               experience_level=experience_level,
                               experience_years=experience_years,
                               plan=plan,
                               nutrition=nutrition,
                               days=days,
                               progress_data=progress_data)
    return render_template('form.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/progress')
def progress():
    return render_template('progress.html')

if __name__ == '__main__':
    app.run(debug=True)
