from flask import Flask
import requests
app = Flask(__name__)
@app.route("/")
@app.route("/hello")
def hello():
    url='https://www.tpex.org.tw/openapi/v1/bond_ISSBD5_data'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3' }
    try:
        r=requests.get(url,headers=headers)
        time.sleep(1)
        if(r.status_code==200):
            r.encoding = 'utf-8'
            html_text=r.text
            return(html_text)
            #get_bond_arr=json.loads(html_text)
    except BaseException as msg:
        return('Network_error!')
