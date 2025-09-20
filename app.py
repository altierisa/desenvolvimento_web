

from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json
import resend

resend.api_key = 're_VkM3kivU_GXxe52LgLCuvsSUh2miV5hxp'
app = Flask(__name__) #instanciamos a aplicacao web
with open ('dados.json','r',encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        nome = request.form['name']
        email=request.form['email']
        mensagem=request.form['message']

#montar o dicionario da nova mensagem
        dados_mensagem={
            'nome':nome,
            'email':email,
            'mensagem':mensagem,
            'data':f'{datetime.today()}'
        }
        #add e salva o json
        dados.append(dados_mensagem) #add e salvar o json
        with open('dados.json','w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
#envia email usando resend
            r= resend.Emails.send= ({
                "from":"onboarding@resend.dev",
                "to":"isabellafrad.alt@gmail.com",
                "subject":f"Solicitação de adocao {nome}",
                "html": f'<p>Email:{email}<br>{mensagem}</p>'
            })
#redireciona para enviar reenvio do formulario
        return redirect(url_for('index'))
    #renderizar a pag -GET
    return render_template('index.html')




if __name__ == '__main__': #asseguramos a independencia do projeto
    app.run(debug=True)


