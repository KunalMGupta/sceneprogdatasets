from HSSD.hssd import AssetRetrieverHSSD
from future.future import AssetRetrieverFuture

class SceneProgAssetRetriever:
    def __init__(self):
        self.hssd = AssetRetrieverHSSD()
        self.future = AssetRetrieverFuture()
    
    def __call__(self, description):
        ## first search in Future
        future_results = self.future.run(description)
        if not future_results == 'No models found':
            return ("FUTURE",future_results)
        
        ## then search in HSSD
        hssd_results = self.hssd.run(description)
        if not hssd_results == 'No models found':
            return ("HSSD",hssd_results)
        
        return "No models found"