import os
import json
from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = "Your OpenAI API Key"

# We need to read or load the PDF document
loader = PyMuPDFLoader('/Users/manuvenugopal/Documents/Working on Docs/Extracting_info_from_tables/Hospital_Report.pdf')
doc = loader.load()

# We now need to create a prompt temple for model to do the task
template = """
Please read and analyze the following text containing hospital information {doc_text}. Your task is to extract the relevant details and create a JSON dictionary with the following keys:

- Hospital name
- Address
- City
- State
- Zip code
- Contact number
- Email Address
- Website

Ensure the output is formatted as a JSON dictionary. The response should contain only the JSON dictionary and no additional text.
"""
prompt = PromptTemplate(template=template, input_variables=["doc_text"])

# After this, we need to create instance of the OpenAI model we are going to use
llm =  ChatOpenAI(model="gpt-4o", temperature=0)

# Now we can create our LangChain with LLM and prompt
llm_chain = LLMChain(llm=llm, prompt= prompt)

for page in doc:
    text = page.page_content
    response = llm_chain.invoke({"doc_text": text})
    #print(response)
    data = response["text"]
    data = data.replace("json", "")
    data = data.replace("`", "")
    data = json.loads(data)
    print(data)