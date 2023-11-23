from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def procesar_ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros_pintura = int(request.form['tarros_pintura'])

        precio_por_tarro = 9000
        total_sin_descuento = tarros_pintura * precio_por_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        descuento_aplicado = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - descuento_aplicado

        return render_template('ejercicio1.html', 
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               descuento=descuento_aplicado,
                               total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def procesar_ejercicio2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['contrasena']

        usuarios = {'juan': 'admin', 'pepe': 'user'}

        if nombre in usuarios and usuarios[nombre] == password:
            if nombre == 'juan':
                mensaje = f"Bienvenido administrador {nombre}"
            elif nombre == 'pepe':
                mensaje = f"Bienvenido usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html', nombre=nombre, mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
