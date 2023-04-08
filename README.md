# chatgpt-discord
深夜帯に深夜テンションですごく適当に書いたやつ。
ライブラリはrevChatGPTを使用。<br>
`pip install revChatGPT`<br>
**注意:非公式な方法でリクエストをしているため、自己責任で行なってください。**
<br>

# AccessTokenの取り方
https://chat.openai.com/api/auth/session にChatGPTにログイン済みのブラウザでアクセスするとJsonが返って来ます。accessTokenってのがAccessTokenなので、それをこのコードでは利用します。<br>

# GPT-4を利用する方法
chatbot.askの部分にmodel="GPT-4"を付け足すと使えます。<br>
Example:<br>
```python
chatbot.ask(query,None,model="GPT-4")
```
ただし、ChatGPT Plusに加入する必要があります。
