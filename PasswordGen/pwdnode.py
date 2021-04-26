from flask import Flask, render_template, redirect, url_for
import generator

app = Flask(__name__)


@app.route('/', methods=['GET'])
def pass_home():
    if generator.passwordStore == []:
        message = "Click on any buttons below.."
        return render_template('base.html', message=message)
    s = ""
    for elem in generator.passwordStore[:16]:
        s += str(elem)
    message = s
    return render_template('base.html', message=message)


@app.route('/generator', methods=['GET'])
def pass_generated():
    if generator.lwc_list == [] and generator.upc_list == [] and generator.nums_list == []:
        return redirect(url_for('pass_home'))
    generator.Password.generate_password()
    return redirect(url_for('pass_home'))


@app.route('/incnum', methods=['GET'])
def pass_num():
    generator.Password.generate_nums()
    message = "Numbers Included.."
    return render_template('base.html', message=message)


@app.route('/incsym', methods=['GET'])
def pass_sym():
    generator.Password.generate_sym()
    message = "Symbols Included.."
    return render_template('base.html', message=message)


@app.route('/inclower', methods=['GET'])
def pass_lower():
    generator.Password.generate_lower_case()
    message = "Lower Case Chars Included.."
    return render_template('base.html', message=message)


@app.route('/incupper', methods=['GET'])
def pass_upper():
    generator.Password.generate_upper_case()
    message = "Upper Case Chars Included.."
    return render_template('base.html', message=message)


@app.route('/clear', methods=['GET'])
def pass_clear():
    del generator.upc_list[:]
    del generator.lwc_list[:]
    del generator.passSymbs[:]
    del generator.nums_list[:]
    del generator.passwordStore[:]
    return redirect(url_for('pass_home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
