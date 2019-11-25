from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    artist = Col('Invoice_Title')
    title = Col('Invoice_Number')
    release_date = Col('Due Date')
    publisher = Col('Name')
    status = Col('Status')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))