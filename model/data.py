from types import MappingProxyType

available_search_categories = MappingProxyType({
    'intitle': 'Title',
    'inauthor': 'Author',
    'inpublisher': 'Publisher',
    'isbn': 'ISBN',
    'lccn': 'LCCN',
    'oclc': 'OCLC'
})