import os
import worker
from common import Resource

def polish():
    text = os.environ['POPCLIP_TEXT']
    type = Resource.GetProofreaderType()
    worker.service(type,
                Resource.GetSystemPrompt(type),
                Resource.GetUserPrompt(type),
                text)

if __name__ == "__main__":
    polish()