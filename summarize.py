import os
import worker
from common import Resource

def summary():
    text = os.environ['POPCLIP_TEXT']
    type = Resource.GetSummaryType()
    lang = os.environ['POPCLIP_OPTION_LANG']
    worker.service(type,
                Resource.GetSystemPrompt(type).replace(Resource.POPCLIP_PROMPT_LANGUAGE_MARK, lang),
                Resource.GetUserPrompt(type).replace(Resource.POPCLIP_PROMPT_LANGUAGE_MARK, lang),
                text)

if __name__ == "__main__":
    summary()
