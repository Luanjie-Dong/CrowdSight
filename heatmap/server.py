from flask import Flask, render_template
# import subprocess
import map

app = Flask(__name__)

@app.route('/')
def index():
    # Run the map.py script to generate the map
    map.create_map()

    # Render the map in an iframe in the HTML template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
