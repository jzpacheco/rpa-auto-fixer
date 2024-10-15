import traceback
import requests

def capturar_dados(codigo):
    try:
        # Aqui você deve colocar a lógica do seu RPA
        exec(codigo)  # Executa o código do RPA (pode gerar um erro)
    except Exception as e:
        # Captura o traceback do erro
        tb_str = traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__)
        traceback_str = ''.join(tb_str)
        
        # Captura o HTML da página (substitua pela lógica de captura do HTML real)
        html = "<html>... seu HTML aqui ...</html>"  # Exemplo; use page.content() para capturar o HTML real
        
        return {
            "html": html,
            "traceback": traceback_str,
            "codigo": codigo
        }

def enviar_para_openai(dados):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": "Bearer sua_chave_api",  # Substitua com sua chave da API
        "Content-Type": "application/json"
    }
    print('Enviando para OpenAI...')
    response = requests.post(url, headers=headers, json={"model": "gpt-4o-mini","messages": [{"role": "user", "content": f'RETURN FIXED CODE ONLY {str(dados)}'}]})
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao enviar para OpenAI: {response.status_code} - {response.text}")
        return None

def tratar_resposta(resposta):
    if resposta:
        # Extraindo o código corrigido da resposta
        codigo_corrigido = resposta.get("choices")[0].get("message").get("content")
        
        # Exibir o código corrigido
        print("Código Corrigido:")
        print(codigo_corrigido)
        
        return codigo_corrigido
    else:
        print("Não foi possível obter uma resposta válida da OpenAI.")
        return None

