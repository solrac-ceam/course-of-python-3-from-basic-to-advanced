from pathlib import Path


caminho_projeto = Path()
print(caminho_projeto.absolute())

print()
caminho_arquivo = Path(__file__)
print(caminho_arquivo.absolute())
print(caminho_arquivo.parent)
print(caminho_arquivo.parent.parent)

print()
ideias = caminho_arquivo.parent / 'ideias'
print(ideias / 'arquivo.txt')

print()
arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
arquivo.touch()  # Cria o arquivo se não existir
print(arquivo)
arquivo.write_text('Olá mundo')
print(arquivo.read_text())
arquivo.unlink()  # Remove o arquivo

print()
caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
with caminho_arquivo.open('a+') as file:
    file.write('uma linha\n')
    file.write('outra linha\n')
    
print(caminho_arquivo.read_text())
caminho_arquivo.unlink()  # Remove o arquivo


print()
caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)  # Cria a pasta se não existir
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)  # Cria a subpasta se não existir

outro_arquivo = subpasta / 'outro_arquivo.txt'
outro_arquivo.touch()  # Cria o arquivo se não existir
outro_arquivo.write_text('Hey')

mais_arquivo = caminho_pasta / 'mais_arquivo.txt'
mais_arquivo.touch()  # Cria o arquivo se não existir
mais_arquivo.write_text('Hey')


def rmtree(root: Path, remove_root: bool = True):
    for item in root.glob('*'):
        if item.is_dir():
            print('DIR:', item)
            rmtree(item, remove_root=False)
            item.rmdir()
        else:
            print('FILE:', item)
            item.unlink()

    if remove_root:
        root.rmdir()

rmtree(caminho_pasta)
