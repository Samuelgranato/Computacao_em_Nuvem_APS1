from flask import Flask, request,jsonify
import json
app = Flask(__name__)


all_tarefas = {}


class Tarefas:
  def __init__(self, name,id):
    self.name = name
    self.done = False
    self.id = id
    self.active = True

  def toJSON(self):
        return json.dumps(self.__dict__)


def get_all_tarefas():
    return all_tarefas

def post_tarefa(nome):
    id = len(get_all_tarefas())
    tarefa = Tarefas(nome,id)

    all_tarefas[id] = tarefa.toJSON()
    return

def delete_tarefa(id):
    tarefa_dict = json.loads(all_tarefas[id])

    nome = tarefa_dict['name']

    tarefa = Tarefas(nome,id)
    tarefa.done = tarefa_dict['done']

    tarefa.active = False

    del all_tarefas[id]

    all_tarefas[id] = tarefa.toJSON()

    return

def get_tarefa(id):
    return all_tarefas[id]

def atualiza_tarefa(id, nome, done):
    tarefa = Tarefas(nome,id)


    if done == False or done == "True":
        tarefa.done = bool(done)

    print(type(id))
    print(all_tarefas)
    del all_tarefas[id]
    all_tarefas[id] = tarefa.toJSON()
    return




@app.route("/")
def home():
    return "OK"


@app.route('/Tarefa',methods=["GET","POST"])
def tarefa():
    if request.method == 'POST': 
        nome = request.args.get('nome')

        post_tarefa(nome)
        return 'ok'
    elif request.method == 'GET':
        return get_all_tarefas() 

@app.route('/Tarefa/<id>',methods=["GET","PUT","DELETE"])
def tarefa_id(id):
    id = int(id)

    if request.method == 'PUT': 
        nome = request.args.get('nome')
        done = request.args.get('done')

        atualiza_tarefa(id,nome,done)
        return 'ok'

    elif request.method == 'GET':
        return get_tarefa(id) 

    elif request.method == 'DELETE':
        delete_tarefa(id) 
        return ('',200)

@app.route('/healthcheck/')
def healthcheck():
    return ('', 200)

if __name__ == '__main__':
    post_tarefa("joao")
    post_tarefa("gabriel")
    post_tarefa("matddeus")

    app.run(host= '0.0.0.0')






    