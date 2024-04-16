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

