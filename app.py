from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página principal (index)
@app.route('/')
def home():
    # Flask buscará automáticamente en la carpeta 'templates'
    return render_template('index.html')

# Ejemplo de otra ruta (por si creas un contacto.html)
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    # debug=True permite que el servidor se reinicie solo al detectar cambios
    app.run(debug=True)
