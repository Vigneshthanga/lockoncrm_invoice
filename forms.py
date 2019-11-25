# forms.py

from wtforms import Form, StringField, SelectField, validators

class MusicSearchForm(Form):
    choices = [('Invoice_Number', 'Invoice_Number'),
               ('Name', 'Name')]
    select = SelectField('Search for Invoice:', choices=choices)
    search = StringField('')


class AlbumForm(Form):
    status = [('Sent', 'Sent'),
                   ('Paid', 'Paid'),
                   ('Cancel', 'Cancel'), 
                   ('pending', 'pending')]
                   
    artist = StringField('Invoice_Title')
    title = StringField('Invoice_Number')
    release_date = StringField('Due Date')
    publisher = StringField('Name')
    status = SelectField('Status', choices=status)
