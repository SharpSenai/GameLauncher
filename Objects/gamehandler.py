from libs import *

class gameHandler():
    
    def __init__(self):
        self.json_Path = Lib_OS.path.join(Lib_OS.path.dirname(__file__),"..","Scripts","gameid.json")
        self.clone_Repository()
    
    def loadGame(self):
        
        
        
        pass
    
    def clone_Repository(self): 
        with open(self.json_Path, "r") as json_File:
            self.launcher_Games = Lib_Json.load(json_File)
            
        self.folder_ToDownload = Lib_OS.path.join(Lib_OS.path.dirname(__file__),"..","GamesDownloaded")
        
        if not Lib_OS.path.exists(self.folder_ToDownload):
            Lib_OS.makedirs(self.folder_ToDownload)
            
        for _,url in enumerate(self.launcher_Games["Repositories"]):
            try:
                print(f"Clonando {url}...")
                Lib_Git.Repo.clone_from(url, self.folder_ToDownload)
            except:
                print(f"Erro ao clonar {url}...")

    