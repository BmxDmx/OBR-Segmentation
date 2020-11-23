import numpy as np
import zlib
import base64
import cv2
from PIL import Image
import io
string = "eJwBTwSw+4lQTkcNChoKAAAADUlIRFIAAAByAAAAjggGAAAA7Y1cHwAABBZJREFUeF7t29F2ozAMRdHy/x+drrQlhQSCJMuW5Jx5jU2Dtq9syJrla+J/t9vtJrm9ZVkWybjMY8rfwFpcKdoZRnVMIP9kgUzQb1rTuL2FqqClE+kJWB0TyIOOUjGVQAIZvznSWv8NSifyfhuemBVb6koJ5FNjqYpZGtIzjY+VXfQtD5AkMvaw0yONlVNZNpFA7oMEJM+RtNbYCkyQyJ5tteo+WbK1AvnaC4A86Y/VXgwACWTcVj+itd7vrlIqSeSb9Qhkx7COSiOJ7Ijo/bPV1VclkVcVavh8ZCIrPVOW2yOBPE4BkILuUKHFAgmkoAIdhtBaJ2itEYhVHkNKtVYgz1sckIL2z2FHUCTNEBJJIjXr5WUsiWwq335yVBqrvN0ps0cC+T4VQAq7Rvb2CiSQwgo4DaO10lpdlhKt1aGM0Wms8JquxB6ZATI7JpCKjpG5vaaHzJJGEqlY8UdDM0FmxkydyGyIQBpTCaS8cCRSXqufkVkPPGkhM6YRSOWqvw8HUlc0EqmrF61VWS8SqSwYiVQWLOs+CSSQhgoIp2Q96KxfP+MjSMpEAilc8ZthQOprlvLkCiSQhgoIp2RvrRlPriRSuLieh2U78AAJpLECgmkVWmu29koiBQvrbEim9poOskoaSeRFAipBZsIkkQ2tFcg3xSORtpVFIm11e8zKcuABEsjGCpxMr9Zas+yTqRJZERHIg0QCae9yJNJeu1QHHiCBdKjA0yVorfaapklkVUQOO5OkEciJIDNg0lrt29JuZvSrOiCBdKrA32UqH3ZorZMgAgmkW1tLsUdWb6skMvF/MddG5eNPrTOkcUWPxAxvrUBqs388PhRyJsTofRJIn0D8XOVjW+tsiYzEJJGOiQTSuZiRl4tqryTSWR1I54JGXQ7IqMp3+LsRmLRWINsqMOOjR+SrurBEAtkWhOfZQPrW83G10fskkEDaKzBzW43aJ0MSCaQ9BGczgfSvacgvIUB2ghzdYodDfkJb3a6NUadXIEmkrQIk0la3q1lDE/lpiCN/aAbyaqk7fD5inwTSAerqEkBeVajQ570xSeSgxTAF5CcecqTrwwu4SyKBkzL+jvPAbIIETAcmGW1FNUOCKGGxjbFgAmmrdddZQyBJYlfD3cU1oKpEgjgOUfszmAgSwPGArpAAxgE+/+WrNnuaSBDzIEqeNXeQ4OXC234bVSKBnAASxLyIotYKYG5A6el1ARLIGhWY8FseHXxIZGHoLSiQs0Cu98FeWVN0TSUvBGr6vXxrIGeEPLonWm4NadHPWOyj+TFVkPfbIaG5UA8PO61fEeTWCurm754jdVPlo0GV18o6cggk+6qe5+o3x3dXVO+R+q/3O4OE7ivXgnZkMAzSE9O7CNbFmWneUEhruwXuesl8A5s7OJ371Hm9AAAAAElFTkSuQmCCX+X2cg=="#

def base64_2_mask(s):
    z = zlib.decompress(base64.b64decode(s))
    n = np.frombuffer(z, np.uint8)
    mask = cv2.imdecode(n, cv2.IMREAD_UNCHANGED)[:, :, 3].astype(bool)
    with open('randomfile.txt','w')as f :
        tempVal = str(mask)
        f.write(tempVal)
    return mask

    
def mask_2_base64(mask):
    img_pil = Image.fromarray(np.array(mask, dtype=np.uint8))
    img_pil.putpalette([0,0,0,255,255,255])
    bytes_io = io.BytesIO()
    img_pil.save(bytes_io, format='PNG', transparency=0, optimize=0)
    bytes = bytes_io.getvalue()
    return base64.b64encode(zlib.compress(bytes)).decode('utf-8')

returnVal = base64_2_mask(string)
print(mask_2_base64(returnVal))