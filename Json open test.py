import json

with open('E:\\PythonProjects\\pythonProject1\\Anime frec list\\term_meta_bank_small.json', encoding='utf-8') as f:
    data = json.load(f)

    for word in f:
        print(f[0])
