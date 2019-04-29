import re


class TextPreprocessing(object):


    def __init__(self):
        self.FLAGS = re.MULTILINE | re.DOTALL

    def hashtag(self,text):
        text = text.group()
        hashtag_body = text[1:]
        if hashtag_body.isupper():
            result = " {} ".format(hashtag_body.lower())
        else:
            result = " ".join([""] + [re.sub(r"([A-Z])",r" \1", hashtag_body, flags=self.FLAGS)])
        return result

    def allcaps(self,text):
        text = text.group()
        return text.lower() + " "

    def re_sub(self,pattern, repl,text):
            return re.sub(pattern, repl, text, flags=self.FLAGS)

    def text_preprocessing(self,text):
        eyes = r"[8:=;]"
        nose = r"['`-]?"

        def re_sub(pattern, repl):
            return re.sub(pattern, repl, text, flags=self.FLAGS)

        text = re_sub(r"https?:\/\/\S+\b|www\.(\w+\.)+\S*", " ")
        text = re_sub(r"@\w+", "user")
        text = re_sub(r"{}{}[)dD]+|[)dD]+{}{}".format(eyes, nose, nose, eyes), "smile")
        text = re_sub(r"{}{}p+".format(eyes, nose), "laugh")
        text = re_sub(r"{}{}\(+|\)+{}{}".format(eyes, nose, nose, eyes), "sad")
        text = re_sub(r"{}{}[\/|l*]".format(eyes, nose), "neutral")
        text = re_sub(r"/"," / ")
        text = re_sub(r"<3","love")
        text = re_sub(r"[-+]?[.\d]*[\d]+[:,.\d]*", " ")
        text = re_sub(r"#\S+", self.hashtag)
        text = re_sub(r"([!?.]){2,}", r"\1 repeat")
        text = re_sub(r"\b(\S*?)(.)\2{2,}\b", r"\1\2 <elong>")
        text = re_sub(r"([A-Z]){2,}", self.allcaps)

        return text.lower()
