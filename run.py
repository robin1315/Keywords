from flask import request, Flask, render_template

from forms import UrlForm
from models import KeywordsCounter

app = Flask(__name__, static_path='/static')


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route to app, display UrlForm and result of precessing url in list
    :return:
    """
    form = UrlForm(request.form)
    result = dict()
    if request.method == 'POST':
        try:
            counter = KeywordsCounter(form.url.data)
            counter.get_keywords()
            result = counter.count_keywords()
        except AttributeError:
            result['Warning'] = 'This site don\'t use keywords'
        except Exception as e:
            result['Error'] = e

    return render_template('index.html', form=form, result_dict=result)


if __name__ == '__main__':
    app.run(debug=False)
