import os
from chatai import ChatOpenAI
from output import Printer

def service(ext_type, sysprompt, userprompt, text):
    model = os.environ['POPCLIP_OPTION_MODEL']
    key = os.environ['POPCLIP_OPTION_APIKEY']
    url = os.environ['POPCLIP_OPTION_BASEURL']
    chat = ChatOpenAI(
        api_key=key,
        base_url=url,
        sys_prompt=sysprompt,
        user_prompt=userprompt,
        model=model
    )
    response_text = chat.query_openai(text)
    p = Printer(content=response_text, work=ext_type)
    p.run()