import re

re.sub('`([^`]*)`', '<code>\g<1></code>', "`inline code`")


match_pattern = '(?:\s{2})'
replacement_pattern = '<br>'

re.sub(match_pattern, replacement_pattern, "this line has two spaces at the end  ")


match_pattern = '^(\S+.*)\n{2}|\n*(\S+.*)\n*|\n{2}(\S+.*)$'
replacement_pattern = '<p>\g<1>\g<2>\g<3></p>'
test_input = """An example paragraph. Containing multiple lines.

A second paragraph.

A third paragraph."""

re.sub(match_pattern, replacement_pattern, test_input)

match_pattern = '\[(.*?)\]\((.*?)\)'
replacement_pattern = '<a href=\"\g<2>\">\g<1></a>'
test_input = "An example link to [jhub](https://jhub4tb3.cas.mcmaster.ca)."

re.sub(match_pattern, replacement_pattern, test_input)

def translate(input_string: str) -> str:
    
    
    
    match_bold_pattern = '\*{2}(.*)\*{2}'
    replacement_bold_pattern = '<strong>\g<1></strong>'    
    
    bold_string = re.sub(match_bold_pattern, replacement_bold_pattern, input_string)
    
    match_italics_pattern = '\*(.*)\*'
    replacement_italics_pattern = '<em>\g<1></em>'    
    
    output_string = re.sub(match_italics_pattern, replacement_italics_pattern, bold_string)    
    
    
    return output_string
  
def translate(input_string: str) -> str:
    
    replace_hyphen_string = re.sub('\s', '-', input_string)
    id_replacement_string = re.sub('\#{1,3}\-*(.*)', '\g<1>', replace_hyphen_string).lower()
    
    match_h3_pattern = '\#{3}\s*(.*)'
    replacement_h3_pattern = '<h3 id="">\g<1></h3>'    
    
    h3_string = re.sub(match_h3_pattern, replacement_h3_pattern, input_string)
    
    match_h2_pattern = '\#{2}\s*(.*)'
    replacement_h2_pattern = '<h2 id="">\g<1></h2>'    
    
    h2_string = re.sub(match_h2_pattern, replacement_h2_pattern, h3_string)
    
    match_h1_pattern = '\#\s*(.*)'
    replacement_h1_pattern = '<h1 id="">\g<1></h1>'    
    
    h1_string = re.sub(match_h1_pattern, replacement_h1_pattern, h2_string)
    
    match_id_pattern = '<h[1-3]>(.*)<\/h[1-3]>'
    replacement_id_pattern = '<h3>\g<1></h3>'    
    
    id_string = re.sub(match_id_pattern, replacement_id_pattern, h1_string)
    
    match_id_rep_pattern = '(<h[1-3]\sid=")(">.*<\/h[1-3]>)'
    replacement_id_rep_pattern = '\g<1>' + id_replacement_string +'\g<2>'
    
    id_replacement = re.sub(match_id_rep_pattern, replacement_id_rep_pattern, id_string)    
    
    output_string = id_replacement
    
    return output_string
