import requests
from io import BytesIO
from PIL import Image
import base64

headers = {
    "apikey": '679WYBz5UZ1zhBlYjJW3H5qyU1ZqbD11'
}

url = "https://api.aiforthai.in.th:7600/superresolution/sr"
response = requests.post(
    url,
    headers=headers,
    files={'file': open('/home/palm/Pictures/20520955.png', 'rb')},
    data={'text': ''}
)
byte_string = bytearray(response.content)
byte_string = BytesIO(byte_string)
ori_image = Image.open(byte_string)
ori_image.show()
print()
