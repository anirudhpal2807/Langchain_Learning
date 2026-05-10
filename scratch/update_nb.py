import json

notebook_path = r"c:\Langchain\Genrativeai\01-Langchainintro.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        if 'gemini-1.5-flash' in source:
            new_source = source.replace('gemini-1.5-flash', 'gemini-2.0-flash')
            # Split back into lines if it was a list of lines
            cell['source'] = [line + '\n' for line in new_source.split('\n')][:-1]
            if new_source.endswith('\n'):
                 cell['source'].append('\n')
            # Actually, LangChain notebook source can be a list of strings or a single string.
            # Let's just keep it simple.
            cell['source'] = [new_source]

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
