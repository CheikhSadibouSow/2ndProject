from flask import Flask , render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = "cheikh"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banque.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
#Definition des Classes :

#-Classe Pour depense
class depense(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   titre = db.Column(db.String(100), nullable=False) 
   montant = db.Column(db.Integer) 
   
   def __init__(self,titre,montant):
       self.titre = titre
       self.montant = montant


#-Classe Pour revenu       
class revenu(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   titre = db.Column(db.String(100), nullable=False) 
   montant = db.Column(db.Integer) 
   
   def __init__(self,titre,montant):
       self.titre = titre
       self.montant = montant
       
       
with app.app_context():
    db.create_all()



#route pour insertion depense
@app.route('/insert_depense', methods=['GET','POST'])
def insert_depense():
   if request.method == 'POST' :
       titre = request.form['titre']
       montant = request.form['montant']
   
       my_data = depense(titre, montant)
       db.session.add(my_data)
       db.session.commit()
       
       flash("Depense ajouter avec succes")

     
       return redirect(url_for('index'))
   
   return redirect(url_for('index'))  

#route pour insertion revenu 
@app.route('/insert_revenu', methods=['GET','POST'])
def insert_revenu():
   if request.method == 'POST' :
       titre = request.form['titre']
       montant = request.form['montant']
   
       my_data = revenu(titre, montant)
       db.session.add(my_data)
       db.session.commit()
       
       flash("Revenu ajouter avec succes")

     
       return redirect(url_for('index'))
   


#route de base
@app.route('/', methods=['GET'])
def index():
    query = request.args.get('query')
    
    if query:
        # Rechercher des dépenses et des revenus dont le titre contient le terme de recherche
        data_depense = depense.query.filter(depense.titre.like(f"%{query}%")).all()
        data_revenu = revenu.query.filter(revenu.titre.like(f"%{query}%")).all()
    else:
        # Si aucun terme de recherche n'est fourni, afficher tous les éléments
        data_depense = db.session.query(depense)
        data_revenu = db.session.query(revenu)

    return render_template('index.html', query=query, data=data_depense, dt=data_revenu)

#route pour modifier depense
@app.route('/update_depense/<int:id>/', methods=['GET','POST'])           
def update_depense(id):
    data_dep = depense.query.get(id)
    if request.method == 'POST' :
     
       data_dep.titre = request.form['titre']
       data_dep.montant = request.form['montant']   
       
       db.session.commit()
       return redirect(url_for('index'))
    else :
        title = "Modification"
        return render_template("editDep.html", title = title , dataDep = data_dep)

#route pour modifier revenu
@app.route('/update_revenu/<int:id>/', methods=['GET','POST'])           
def update_revenu(id):
    data_rev = revenu.query.get(id)
    if request.method == 'POST' :
     
       data_rev.titre = request.form['titre']
       data_rev.montant = request.form['montant']   
       
       db.session.commit()
       return redirect(url_for('index'))
    else :
        title = "Modification"
        return render_template("editRev.html", title = title , dataRev = data_rev)


#route pour supprimer depense
@app.route('/delete_depense/<int:id>/', methods=['GET','POST'])           
def delete_depense(id):
    del_depense = depense.query.get(id)
    try:
        db.session.delete(del_depense)
        db.session.commit()    
        return redirect('/')
    except :
        return "Une erreur s'est produite !!!"

#route pour supprimer revenu
@app.route('/delete_revenu/<int:id>/', methods=['GET','POST'])           
def delete_revenu(id):
    del_revenu = revenu.query.get(id)
    try:
        db.session.delete(del_revenu)
        db.session.commit()    
        return redirect('/')
    except :
        return "Une erreur s'est produite !!!"
    


#route pour la page about     
@app.route('/about/')
def about():
    return render_template('about.html')

#route pour la page d'ajout depense
@app.route('/ajoutDepense/')
def ajoutDepense():
    return render_template('ajoutDepense.html')


#route pour la page d'ajout revenu
@app.route('/ajoutRevenu/')
def ajoutRevenu():
    return render_template('ajoutRevenu.html') 
   
# Lancement du serveur Flask
if __name__ == "__main__" :
    app.run(debug=True)
  