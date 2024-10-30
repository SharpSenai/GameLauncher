from libs import *
from Objects.pySideUI import GameWindow

'''
def criar_EstruturaTemp(path_tempClone, repo_Url):
    if Lib_OS.path.exists(path_tempClone):
        Lib_Shutil.rmtree(path_tempClone)
    
    Lib_Git.Repo.clone_from(repo_Url, path_tempClone)
    
    Estrutura = []
    
    for dirPath, dirName, fileName in Lib_OS.walk(path_tempClone):
        for name in dirName + fileName:
            path_relative = Lib_OS.path.relpath(Lib_OS.path.join(dirPath, name), path_tempClone)
            Estrutura.append(path_relative)
            
    Lib_Shutil.rmtree(path_tempClone)
    return Estrutura

def sincronizar_Repositorio(local_Path, repo_Url):
    path_tempClone = Lib_OS.path.join(local_Path, "temp_clone")
    estrutura_Temp = criar_EstruturaTemp(path_tempClone, repo_Url)
    
    Estrutura = []
    
    for dirpath, dirnames, filenames in Lib_OS.walk(local_Path):
        for name in dirnames + filenames:
            relative_path = Lib_OS.path.relpath(Lib_OS.path.join(dirpath, name), local_Path)
            Estrutura.append(relative_path)

    jogos_Faltando = [item for item in estrutura_Temp if item not in Estrutura]
    
    if jogos_Faltando:
        print(f"Atualizando {repo_Url}")
        
        if not Lib_OS.path.exists(local_Path):
            Lib_OS.makedirs(local_Path)
            
        repo = Lib_Git.Repo(local_Path)
        repo.git.pull()
    else:
        print("Já atualizado!")
'''

class gameHandler():
    
    def __init__(self):
        self.launcher_Games = None
        self.folder_ToDownload = None
        self.json_Path = Lib_OS.path.join(Lib_OS.path.dirname(__file__),"..","Scripts","gameid.json")
        self.clone_Repository()
        self.gameWindow = None
    
    def loadGame(self, gameName):
        gamePath = Lib_OS.path.abspath(f"GamesDownloaded\\html-css-javascript-games\\{gameName}\\index.html")
        self.gameWindow = GameWindow("2048",gamePath)
        self.gameWindow.show()
    
    def clone_Repository(self): 
        with open(self.json_Path, "r") as json_File:
            self.launcher_Games = Lib_Json.load(json_File)
            
        self.folder_ToDownload = Lib_OS.path.join(Lib_OS.path.dirname(__file__),"..","GamesDownloaded")
        
        if not Lib_OS.path.exists(self.folder_ToDownload):
            Lib_OS.makedirs(self.folder_ToDownload)
            
        for _,url in enumerate(self.launcher_Games["Repositories"]):
            repo_Name = url.split("/")[-1].replace(".git","")
            repo_Path = Lib_OS.path.join(self.folder_ToDownload, repo_Name)
            
            if Lib_OS.path.exists(repo_Path): 
                print(f"{url} já baixado, continuando..")
                continue
            else:
                try:
                    Lib_OS.makedirs(repo_Path, exist_ok=True)
                    Lib_Git.Repo.clone_from(url, repo_Path)
                    #sincronizar_Repositorio(repo_Path, url)
                    print(f"Clonando {url}...")
                except Exception as e:
                    print(f"Erro ao clonar: {url}: {e} | continuando...")
                    continue
                
                    
        self.loadGame()

    