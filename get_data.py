import requests
import pandas as pd

def get_data(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "CEP not found"}

users_path = "01-bronze-raw/users.csv"
users_df = pd.read_csv(users_path)

cep_list = users_df["cep"].tolist()

cep_info_list = []

for cep in cep_list:
    cep_clean = cep.replace("-", "")
    data  = get_data(cep_clean)
    print(data)
    if "erro" in data:
        continue
    cep_info_list.append(data)

cep_info_df = pd.DataFrame(cep_info_list)
cep_info_df.to_csv("01-bronze-raw/cep_info.csv", index=False)
