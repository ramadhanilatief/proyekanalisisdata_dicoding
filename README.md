# Setup Environment
```
!git clone https://github.com/ramadhanilatief/proyekdicoding.git

!pip install pyngrok
!pip install -r "/content/proyekdicoding/requirements.txt"

import os
from threading import Thread
from pyngrok import ngrok

ngrok.set_auth_token("2sXBPs8R1Hjfg46ielV44JIXVmt_7oFCdbj31bwGimDjkSAde")
```
# Run streamlit app
```
def run_streamlit():
    os.system('streamlit run /content/proyekdicoding/dashboard.py --server.port 8501')

thread = Thread(target=run_streamlit)
thread.start()

public_url = ngrok.connect(addr='8501', proto='http', bind_tls=True)
print('Your Streamlit app is live at:', public_url)
```
