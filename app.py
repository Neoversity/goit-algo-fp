from flask import Flask, render_template, request, jsonify
from tasks import task_1, task_2, task_3, task_4, task_5, task_6, task_7

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_task', methods=['POST'])
def run_task():
    task_id = request.json['task_id']
    response = ""
    if task_id == 1:
        response = task_1()
    elif task_id == 2:
        level = int(request.json.get('level', 4))
        response = task_2(level)
    elif task_id == 3:
        num_nodes = int(request.json.get('num_nodes', 11))
        num_edges = int(request.json.get('num_edges', 15))
        start_node = request.json.get('start_node', '1')
        response = task_3(num_nodes, num_edges, start_node)
    elif task_id == 4:
        heap_array = request.json.get('heap_array', [0, 1, 4, 3, 5, 10])
        response = task_4(heap_array)
    elif task_id == 5:
        heap_array = request.json.get('heap_array', [0, 1, 4, 3, 5, 10])
        traversal_method = request.json.get('traversal_method', 'DFS')
        response = task_5(heap_array, traversal_method)
    elif task_id == 6:
        budget = int(request.json.get('budget', 100))
        response = task_6(budget)
    elif task_id == 7:
        response = task_7()
    return jsonify({'status': 'Task executed successfully', 'output': response})

if __name__ == '__main__':
    app.run(debug=True)
