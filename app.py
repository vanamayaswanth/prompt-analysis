from flask import Flask, render_template, request
from app_util import prompt_analysis

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        api_key = request.form['openai_key']
        temp=request.form['temp']
        # model=request.form['model']
        max_token=request.form['max_token']
        prompt = request.form['prompt']
        score, new_prompt = prompt_analysis(query=prompt,api_key=api_key,temp=temp,max_token=max_token)
        return render_template('result.html', score=score,new_prompt=new_prompt)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
