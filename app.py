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
    input_param = ''
    if request.method == 'POST':
        code = request.form.get('code_in')  # access the data inside
        tokenizer = Tokenizer(code)
        parser = Parser(tokenizer)
        interpreter = Interpreter(parser)
        try:
            input_param = request.form.get('input_in')
            interpreter.input = input_param.split(',')
            interpreter.interpret()
            output = interpreter.output
            interpreter.input = []
        except Exception as e:
            output = e
            print(e)

    return render_template('cfpl.html', message=code, input=input_param, output=output)


if __name__ == '__main__':
    app.run(debug=True)
