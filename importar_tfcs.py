import os
import json
import django

# Configurar ambiente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import TFC

def carregar_tfcs():
    caminho = 'data/tfcs.json'
    
    

    with open(caminho, 'r', encoding='utf-8') as f:
        dados = json.load(f)
        
        # Se o JSON for um único objeto (como o que enviou)
        if isinstance(dados, dict):
            itens = [dados]
        else:
            itens = dados

        for item in itens:
           
        
            texto_completo = item.get('texto', '')
            
            TFC.objects.create(
                titulo=item.get('titulo'),
                orientadores=item.get('orientador'),
                resumo=item.get('resumo'),
                link_pdf=item.get('pdf'),
                imagem_url=item.get('imagem'),
                rating=item.get('rating', 0),
                ano=2025 
            )
            print(f"Importado com sucesso: {item.get('titulo')}")

if __name__ == '__main__':
    carregar_tfcs()