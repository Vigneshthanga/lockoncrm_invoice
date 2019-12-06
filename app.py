# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_url_path='/invoice/static')
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://invoice:commonsyspass@192.168.33.15:3306/invoice"
app.secret_key = "flask rocks!"

db = SQLAlchemy(app)

from db_setup import init_db, db_session
from forms import MusicSearchForm, AlbumForm
from flask import flash, render_template, request, redirect
from models import Album, Artist
from tables import Results

#init_db()

@app.route('/invoice/home')
def home():
    return render_template('home.html')

@app.route('/invoice/contact')
def contact():
    return render_template('contact.html')

@app.route('/invoice/about')
def about():
    return render_template('about.html')

@app.route('/invoice/charts')
def charts():
    return render_template('charts.html')

@app.route('/invoice/search')
def search():
    return render_template('search.html')

@app.route('/invoice', methods=['GET', 'POST'])
def index():
    search = MusicSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)

@app.route('/invoice/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
        qry = db_session.query(Album)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/invocie')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)


@app.route('/invoice/new_album', methods=['GET', 'POST'])
def new_album():
    """
    Add a new album
    """
    form = AlbumForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        album = Album()
        save_changes(album, form, new=True)
        flash('Album created successfully!')
        return redirect('/invoice')

    return render_template('new_album.html', form=form)

def save_changes(album, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    artist = Artist()
    artist.name = form.artist.data

    album.artist = artist
    album.title = form.title.data
    album.release_date = form.release_date.data
    album.publisher = form.publisher.data
    album.status = form.status.data


    if new:
        # Add the new album to the database
        db_session.add(album)

    # commit the data to the database
    db_session.commit()

@app.route('/invoice/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Album).filter(
                Album.id==id)
    album = qry.first()

    if album:
        form = AlbumForm(formdata=request.form, obj=album)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(album, form)
            flash('Album updated successfully!')
            return redirect('/')
        return render_template('edit_album.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)


if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run()
