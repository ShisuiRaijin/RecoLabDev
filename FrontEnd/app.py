from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/registro')
def registro():
    return render_template("formulario.html")

@app.route('/tiendas/<int:tienda>/productos/nuevo')
def cargar_producto(tienda):
    return render_template("carga_producto.html", id_tienda=tienda)

@app.route('/tiendas/<int:tienda>')
def tienda_public(tienda):
    return render_template("vista_publico_tienda.html", id_tienda=tienda)

@app.route('/tiendas/<int:tienda>/editar')
def tienda_user(tienda):
    return render_template("vista_usuario_tienda.html", id_tienda=tienda)

if __name__ == '__main__':
    app.run(debug=True, port=80)
