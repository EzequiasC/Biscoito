import requests

def gerar_biscoito_zen():
    try:
        resposta = requests.get("https://zenquotes.io/api/random")
        if resposta.status_code == 200:
            dados = resposta.json()[0]
            return f"{dados['q']} — {dados['a']}"
        else:
            return "Não foi possível obter seu biscoito agora."
    except:
        return "Erro de conexão. Tente novamente mais tarde."

# Execução
print("🍪 Seu biscoito da sorte:", gerar_biscoito_zen())

# Adiciona um "input" para pausar a execução e aguardar o usuário pressionar Enter
input("\nPressione Enter para sair...")
