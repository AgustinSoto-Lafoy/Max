from flask import Flask, render_template  # Importar Flask para que permita crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

#Usted solo modifique de aqui para abajo

@app.route('/')          # El decorador "@" asocia la ruta con la función siguiente
def hello_world():
    return render_template("index.html")  # Retorna la cadena 'Hello World!' como respuesta

@app.route('/bye')          # El decorador "@" asocia la ruta con la función siguiente
def bye_world():
    return render_template("bye.html")

#Usted solo modifique de aqui para arriba

if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depuracion