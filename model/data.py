from types import MappingProxyType

available_search_keyword = MappingProxyType({
    'intitle': 'Title',
    'inauthor': 'Author',
    'inpublisher': 'Publisher',
    'isbn': 'ISBN',
    'lccn': 'LCCN',
    'oclc': 'OCLC'
})