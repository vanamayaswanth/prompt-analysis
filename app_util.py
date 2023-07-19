

import openai
from openai.error import InvalidRequestError
import json



def classify(chat,api_key):
    try:
        openai.api_key = api_key
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.3,
            messages=[
                {
                    "role": "system",
                    "content": 
                        """
                    You need to analyze the given prompt and provide a score on the scale of 1 to 100 based on the following parameters:. 
                        The given prompt should be clear and specific, using complete sentences. The prompt might have  provide context.. 
                        The prompt might have  system and user instructions .\n4. The prompt might  have explicit cues.. The prompt should be  broken down for  complex tasks 
                        or limit the scope.Now, generate a new_prompt that satisfies all the parameters, and provide the output as a vaild  JSON  object with the keys 
                        'score' and 'new_prompt
                    """
                },
                {"role": "user", "content": f"{str(chat)}"},
            ],
        )

        dic= json.loads(res["choices"][0]["message"]["content"])
        
        score=dic["score"]
        new_prompt=dic["new_prompt"]

        return score, new_prompt
        
        

    except InvalidRequestError:
        print("Token exceeded")

    except Exception as e:
        raise e
    