from flask import Flask, redirect, render_template, request, url_for

from app_util import prompt_analysis
from app_util import CustomModeration

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        option = request.form["option"]
        if option == "openai":
            return redirect(url_for("openai"))
        elif option == "huggingface":
            return redirect(url_for("huggingface"))
        elif option == "about":
            return redirect(url_for("about"))
    return render_template("index.html")


@app.route("/openai", methods=["GET", "POST"])

# def openai():
#     if request.method == "POST":
#         api_key = request.form["api_key"]
#         temp = request.form["temp"]
#         max_token = request.form["max_token"]
#         prompt = request.form["prompt"]
        
#         try:
#             # Use custom moderation
#             moderation_result = CustomModeration().run(prompt)  # Run custom moderation
            
#             if isinstance(moderation_result, str):
#                 # If there is an error message, display it on the result page
#                 return render_template(
#                     "moderation_result.html",
#                     moderation_result=moderation_result,
#                 )
            
#             # If no error, perform analysis and show normal result page
#             score, new_prompt = prompt_analysis(
#                 query=prompt, api_key=api_key, temp=temp, max_token=max_token
#             )
#             return render_template(
#                 "result.html",
#                 moderation_result=None,
#                 api_key=api_key,
#                 temp=temp,
#                 max_token=max_token,
#                 prompt=prompt,
#                 score=score,
#                 new_prompt=new_prompt,
#             )
#         except Exception as e:
#             # Handle exceptions and display error message on the result page
#             return render_template(
#                 "moderation_result.html",
#                 moderation_result=str(e),  # Pass the exception message as moderation_result
#             )
#     return render_template("openai.html")




def openai():
    if request.method == "POST":
        # Ensure that the API key and other form inputs are obtained from the form
        openai_api_key = request.form["api_key"]
        temp = request.form["temp"]
        max_token = request.form["max_token"]
        prompt = request.form["prompt"]
        
        try:
            # Create an instance of CustomModeration with the API key
            moderation = CustomModeration(openai_api_key)
            
            # Use custom moderation
            moderation_result = moderation.run(prompt)  # Run custom moderation
            
            if moderation_result:
                # If there is an error message, display it on the moderation_result page
                return render_template(
                    "moderation_result.html",
                    moderation_result=moderation_result,
                )
            
            # If no error, perform analysis and show normal result page
            score, new_prompt = prompt_analysis(
                query=prompt, api_key=openai_api_key, temp=temp, max_token=max_token
            )
            return render_template(
                "result.html",
                moderation_result=None,
                api_key=openai_api_key,
                temp=temp,
                max_token=max_token,
                prompt=prompt,
                score=score,
                new_prompt=new_prompt,
            )
        except Exception as e:
            # Handle exceptions and display error message on the moderation_result page
            return render_template(
                "moderation_result.html",
                moderation_result=str(e),  # Pass the exception message as moderation_result
            )
    return render_template("openai.html")




@app.route("/huggingface", methods=["GET", "POST"])
def huggingface():
    if request.method == "POST":
        hugging_key = request.form["hugging_key"]
        temp = request.form["temp"]
        max_token = request.form["max_token"]
        prompt = request.form["prompt"]
        return redirect(
            url_for(
                "result",
                option="huggingface",
                hugging_key=hugging_key,
                temp=temp,
                max_token=max_token,
                prompt=prompt,
            )
        )
    return render_template("huggingface.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        option = request.form["option"]
        if option == "connection":
            return redirect(url_for("connection"))
    return render_template("about.html")


@app.route("/connection")
def connection():
    return render_template("connection.html")


@app.route("/result", methods=["GET"])
def result():
    option = request.args.get("option")
    if option == "openai":
        api_key = request.args.get("api_key")
        temp = request.args.get("temp")
        max_token = request.args.get("max_token")
        prompt = request.args.get("prompt")

        check_moderation(api_key=api_key,query=prompt)
        score, new_prompt = prompt_analysis(
            query=prompt, api_key=api_key, temp=temp, max_token=max_token
        )
        return render_template(
            "result.html", option="OpenAI", score=score, new_prompt=new_prompt
        )
    # elif option == "huggingface":
    #     hugging_key = request.args.get("hugging_key")
    #     temp = request.args.get("temp")
    #     max_token = request.args.get("max_token")
    #     prompt = request.args.get("prompt")
    #     score, new_prompt = prompt_analysis(
    #         query=prompt, hugging_key=hugging_key, temp=temp, max_token=max_token
    #     )
    #     return render_template(
    #         "result.html", option="Hugging Face", score=score, new_prompt=new_prompt
    #     )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
