# Stock_Berman
Mathew_Berman's implemtation modified for local use with Ollama
From his tutorial video https://www.youtube.com/watch?v=iJjSjmZnNlI&ab_channel=MatthewBerman 

Notes on how to use this (I don't understand poetry, so this might be screwed up)
```
pip install python-dotenv
pip install crewai
pip install crewai-tools
poetry lock
cd src
poetry run financial_analyst_crew
```

Yup is screwed up (wants a password and install kde wallet?!?)
I'm going back conda

```
conda create -n Stock_Berman
conda activate Stock_Perman
pip install crewai
pip install crewai-tools
pip install -U langchain-community
cd src
python main.py
```

__Currently getting timeout errors__
```
python main.py
/home/chris/.local/lib/python3.10/site-packages/langchain/llms/__init__.py:548: LangChainDeprecationWarning: Importing LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.llms import Ollama`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
 [DEBUG]: == Working Agent: Financial Researcher

 [INFO]: == Starting Task: Use a search tool to look up this company's stock information: Tesla. The goal is to prepare enough information to make an informed analysis of the company's stock performance.



> Entering new CrewAgentExecutor chain...
Traceback (most recent call last):
  File "/home/chris/.local/lib/python3.10/site-packages/urllib3/connection.py", line 198, in _new_conn
    sock = connection.create_connection(
  File "/home/chris/.local/lib/python3.10/site-packages/urllib3/util/connection.py", line 85, in create_connection
    raise err
  File "/home/chris/.local/lib/python3.10/site-packages/urllib3/util/connection.py", line 73, in create_connection
    sock.connect(sa)
TimeoutError: [Errno 110] Connection timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/chris/.local/lib/python3.10/site-packages/urllib3/connectionpool.py", line 793, in urlopen
    response = self._make_request(
  File "/home/chris/.local/lib/python3.10/site-packages/urllib3/connectionpool.py", line 491, in _make_request
    raise new_e
  File "/home/chris/.local/lib/python3.10/site-packages/urllib3/connectionpool.py", line 467, in _make_request
    self._validate_conn(conn)
  File "/home/chris/.local/lib/python3.10/site-packages/urllib3/connectionpool.py", line 1099, in _validate_conn
    conn.connect()
  File "/home/chris/.local/lib/python3.10/site-packages/urllib3/connection.py", line 616, in connect
    self.sock = sock = self._new_conn()
  File "/home/chris/.local/lib/python3.10/site-packages/urllib3/connection.py", line 207, in _new_conn
    raise ConnectTimeoutError(
urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x7f5ed2dcfa90>, 'Connection to 11434 timed out. (connect timeout=None)')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/chris/.local/lib/python3.10/site-packages/requests/adapters.py", line 486, in send
    resp = conn.urlopen(
  File "/home/chris/.local/lib/python3.10/site-packages/urllib3/connectionpool.py", line 847, in urlopen
    retries = retries.increment(
  File "/home/chris/.local/lib/python3.10/site-packages/urllib3/util/retry.py", line 515, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='11434', port=443): Max retries exceeded with url: /api/generate (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x7f5ed2dcfa90>, 'Connection to 11434 timed out. (connect timeout=None)'))
```
