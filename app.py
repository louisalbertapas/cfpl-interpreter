from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def interpret_code():
    message = ''
    output = ''
    if request.method == 'POST':
        message = request.form.get('code_in')  # access the data inside
        output = message

    return render_template('cfpl.html', message=message, output=output)


if __name__ == '__main__':
    app.run(debug=True)
