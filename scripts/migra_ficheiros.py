import os
import django
from django.core.files import File

# 1. Configura o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings') 
django.setup()

# 2. Importações exatas baseadas nas tuas pastas
from escola.models import Curso
from portfolio.models import UnidadeCurricular, Tecnologia, Projeto, MakingOf
from artigos.models import Artigo  # Agora importado da app correta

def migrar_modelo(classe_model, nome_campo_imagem):
    print(f"\n--- A processar: {classe_model.__name__} ---")
    objetos = classe_model.objects.all()
    
    count = 0
    for obj in objetos:
        campo = getattr(obj, nome_campo_imagem)
        
        # Verifica se o objeto tem um ficheiro associado
        if campo and campo.name:
            try:
                # O campo.path tenta encontrar o ficheiro na pasta media local
                local_path = campo.path
                if os.path.exists(local_path):
                    with open(local_path, 'rb') as f:
                        # Ao fazer .save(), o django-cloudinary-storage faz o upload
                        campo.save(
                            os.path.basename(local_path),
                            File(f),
                            save=True
                        )
                    print(f"✅ Migrado com sucesso: {obj}")
                    count += 1
                else:
                    print(f"⚠️ Ficheiro não encontrado localmente: {local_path}")
            except Exception as e:
                print(f"❌ Erro ao processar {obj}: {e}")
        else:
            print(f"⚪ Sem imagem: {obj}")
    
    print(f"Concluído: {count} imagens migradas para {classe_model.__name__}.")

if __name__ == "__main__":
    # Mapeamento de Classe -> Nome do campo de imagem
    tarefas = [
        (Artigo, 'imagem'),
        (Curso, 'imagem'),
        (UnidadeCurricular, 'imagem'),
        (Tecnologia, 'logo'),
        (Projeto, 'imagem'),
        (MakingOf, 'foto_caderno'),
    ]

    for modelo, campo in tarefas:
        try:
            migrar_modelo(modelo, campo)
        except Exception as e:
            print(f"🔥 Erro crítico no modelo {modelo.__name__}: {e}")

    print("\n🚀 Script finalizado!")