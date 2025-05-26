from types import MappingProxyType

available_search_categories = MappingProxyType({
    'intitle': 'Title',
    'isbn': 'ISBN',
    'lccn': 'LCCN',
    'oclc': 'OCLC',
    'inauthor': 'Author',
    'inpublisher': 'Publisher'
})