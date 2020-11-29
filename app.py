# cfpl imports
from cfpl.Tokenizer import Tokenizer
from cfpl.Parser import Parser
from cfpl.Interpreter import Interpreter

# flask imports
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def interpret_code():
    code = ''
    output = ''
    if request.method == 'POST':
        code = request.form.get('code_in')  # access the data inside
        tokenizer = Tokenizer(code)
        parser = Parser(tokenizer)
        interpreter = Interpreter(parser)
        try:
            interpreter.interpret()
            output = interpreter.output
        except Exception as e:
            print(e)

    return render_template('cfpl.html', message=code, output=output)


if __name__ == '__main__':
    app.run(debug=True)
