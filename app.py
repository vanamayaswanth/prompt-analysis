from flask import Flask, render_template, request
from app_util import classify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        openai_key = request.form['openai_key']
        prompt = request.form['prompt']
        score, new_prompt = classify(prompt,openai_key)
        return render_template('result.html', score=score,new_prompt=new_prompt)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
