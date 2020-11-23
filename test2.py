import base64
code_string ="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"
with open('decoded1.txt','w') as f:
    data = base64.b64decode(code_string)
    f.write(str(data))

