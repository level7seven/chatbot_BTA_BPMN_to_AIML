import lxml.etree as ET
import os


def transform_bpmn_to_simple_bpmn(file_name_input):

    path = os.path.join(file_name_input)
    caminho_absoluto = os.path.abspath(path)

    dom = ET.parse(caminho_absoluto, ET.XMLParser(encoding='utf-8'))
    xslt = ET.parse("xslt/xslt_bpmn_io.xsl")
    transform = ET.XSLT(xslt)
    new_dom = transform(dom)

    # get output file name
    list_file_name = file_name_input.split('\\')
    only_last_name = list_file_name[-1]
    output_file_name = os.path.join("bpmn_simplified/" + only_last_name)
    print(output_file_name)
    new_dom.write(output_file_name)

    return output_file_name



