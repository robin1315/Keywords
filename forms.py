from wtforms import Form, StringField, validators


class UrlForm(Form):
    """
    Form for get url address.
    """
    url = StringField('URL', validators=[validators.url('Sorry this is not url address!'), validators.data_required()])
