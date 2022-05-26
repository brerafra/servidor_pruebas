app = Flask(__name__)

@app.route('/comando/', methods=['GET','POST'])
def comando():
    global reset

    if request.method == 'POST':
        json_data = request.json
        datos = json_data["datos"]
        comando = datos['comando']
        if  comando == '1':
            reset = 2
            #os.system("shutdown -t 0 -r -f")
            return jsonify({"message":"Comando aceptado, reiniciando"})
        else:
            return jsonify({"message":"comando no identificado"})

        #print(json_data)

    return jsonify({"message":"error en recepcion!"})