
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain import LLMChain
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import openai


# llm = OpenAI(temperature=temp,model=model,max_token=max_token)


def prompt_analysis(query,api_key,model,max_token,temp):
    
    openai.api_key=api_key
    llm = OpenAI(temperature=temp,model=model,max_token=max_token)

    prompt = """
    You need to analyze the given prompt {query} and provide a score on the scale of 1 to 100 based on the following parameters:. 
    The given prompt should be clear and specific, using complete sentences. The prompt might have  provide context.. 
    The prompt might have  system and user instructions .\n4. The prompt might  have explicit cues.. The prompt should be  broken down for  complex tasks 
    or limit the scope.Now, generate a new_prompt that satisfies all the parameters,{format_instructions}

    """

    response_schemas = [
        ResponseSchema(name="score",description="this is the score for the given prompt"),
        ResponseSchema(name="new_prompt",description="this is the new prompt for the given prompt")
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

    format_instructions = output_parser.get_format_instructions()

    example_prompt = PromptTemplate(input_variables=["query"],template=prompt,
    partial_variables={"format_instructions": format_instructions})


    _input = example_prompt.format_prompt(query=query)
    output = llm(_input.to_string())

    x= output_parser.parse(output)
    
    score=x["score"]
    
    new_prompt=x["new_prompt"]

    return score,new_prompt
