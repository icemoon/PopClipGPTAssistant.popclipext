import os

class Resource:
    POPCLIP_PROMPT_LANGUAGE_MARK = "POPCLIP_PROMPT_LANGUAGE"

    __proofreader_type = "proofreader"
    __summary_type = "summary"
    __developer_type = "developer"

    __print_title_dict = {
        __proofreader_type:'Polish',
        __summary_type:'Summary',
        __developer_type:'Code Explain'
    }

    __system_content_dict = {
        __proofreader_type:'I want you to act as a proofreader. I will provide you texts and I would like you to review them for any spelling, grammar, or punctuation errors and polish the texts. Your response should be in language same as the texts',

        __summary_type:'Your output should use the following template:\n### Summary\n### Facts\n- [Emoji] Bulletpoint\nYour task is to summarize the text I give you in up to seven concise bullet points, starting with a short, high-quality summary. Pick a suitable emoji for every bullet point. Your response should be in ' + POPCLIP_PROMPT_LANGUAGE_MARK,

        __developer_type:'Your output should use the following template:\n### Code Explain\n- [Emoji] Bulletpoint\n### Bugs\n- [Emoji] Bulletpoint\nYour task is to explain the code I give you. then check and find the bugs of the code. Pick a suitable emoji for every bullet point. Your response should be in ' + POPCLIP_PROMPT_LANGUAGE_MARK
    }

    __user_content_fi_dict = {
        __proofreader_type:'Please correct the grammar and polish the following sentences, do not provide any translation, comments, or notes. Your response should be in language same as the following text:',

        __summary_type:'Your response should be in ' + POPCLIP_PROMPT_LANGUAGE_MARK + ', the text I gave you is:',

        __developer_type: 'Your response should be in ' + POPCLIP_PROMPT_LANGUAGE_MARK + ', the code I gave you is:'
    }

    __icon_name_dict = {
        __proofreader_type:':assets:polish-graph.svg',

        __summary_type:':assets:summary-graph.svg',

        __developer_type:':assets:code-graph.svg'
    }

    @classmethod
    def GetSystemPrompt(cls, type):
        return cls.__system_content_dict[type]

    @classmethod
    def GetUserPrompt(cls, type):
        return cls.__user_content_fi_dict[type]

    @classmethod
    def GetIconName(cls, type):
        return cls.__icon_name_dict[type]

    @classmethod
    def GetPrintTitle(cls, type):
        return cls.__print_title_dict[type]

    @classmethod
    def GetProofreaderType(cls):
        return cls.__proofreader_type

    @classmethod
    def GetSummaryType(cls):
        return cls.__summary_type

    @classmethod
    def GetDeveloperType(cls):
        return cls.__developer_type
