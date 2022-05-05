#Understanding Lexers
from webbrowser import get
from pygments import lexers
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# lexers splits the code into tokens (identifier, keyword, literal etc)

# lex = lexers.get_lexer_by_name("python")
# print(lex)
lex1 = list(get_all_lexers())
print(len(lex1))
LEXERS = [item for item in get_all_lexers() if item[1]]

# print(LEXERS)
# for item in LEXERS:
	# print(item[1])

lex=('JSON-LD', ('jsonld', 'json-ld'), ('*.jsonld',), ('application/ld+json',))
for item in lex:
	print(item[0])



	# ('ABAP', ('abap',), ('*.abap', '*.ABAP'), ('text/x-abap',))

# print(LEXERS)
# print(len(LEXERS))
# # # 
# for item in get_all_lexers():
	
#     print((item[1]))
	# if item[1]:
	#     print(item)
		
#     #    ('ANSYS parametric design language', ('ansys', 'apdl'), ('*.ans',), ())

LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# print(LANGUAGE_CHOICES)

STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
# print(STYLE_CHOICES)

