#from Protocole_complet import search_wiki_
#from ipynb.fs.full.Protocole_complet import search_wiki_
# from scrap_on_google_ import simple_scraper, advanced_scraper
# from similarity_measure_ import compute_best_terms, compute_best_doc
# from ipynb.fs.full.applyBiotex import biotex_terms_extractor
from scrap_on_google_ import simple_scraper, advanced_scraper
from similarity_measure_ import compute_best_terms, compute_best_doc

# spatial_extent = '' # name of the corrsponding territory
# extend_voc_concept = '' # extended vocabulary concept file
# mgdb,mgcol = '','' db and collection name
#########
def main_proto(spatial_extent,voc_concept):
#     spatial_extent = 'Burkina'
#     voc_concept = './voc_concept/agriculture.txt'
    mgdb,mgcol = 'inventaire_medo', 'agriculture_demo' # parameters to be set initially
    #advanced_scraper(spatial_extent,voc_concept)
    advanced_scraper(spatial_extent,voc_concept,mgdb,mgcol)

# if __name__=="main":
#     main_proto()