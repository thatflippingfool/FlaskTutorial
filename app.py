# Import Flask and templates
from flask import Flask, render_template, request

# Create Flask object
app = Flask(__name__)


# Url addresses are assigned by function decoration
@app.route('/')
@app.route('/index')
def index():

    # Generate html
    return render_template('index.html', message='Hello World!')


# Print out some of the contents of the uploaded file
@app.route('/echo', methods=['POST', 'GET'])
def echo():

    # Check that it is a POST request
    if request.method == 'POST':

        # Confirm a file is uploaded
        if 'file' not in request.files:
            return render_template('echo.html', echo='No file uploaded!')

        # Read out some of the file contents
        file = [line.decode() for line in request.files['file'].readlines(1000)]
        return render_template('echo.html', echo=''.join(file))

    # GET request
    return render_template('echo.html', echo='')


# Enable python script to be executable
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run()
