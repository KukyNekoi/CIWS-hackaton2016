# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/jvarred/.spyder2/.temp.py
"""

import urllib
from lxml import html
from lxml import etree
import json
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

def main_process(url):
    page = html.fromstring(urllib.urlopen(url).read())
    headers = [None]
    for item in page.xpath("//table[@class='tabla']/thead/tr"):
        for item2 in item.xpath("th"):
            text = item2.text.strip()
            headers.append(text)
    sys.stdout.write("INSERT DATA{	GRAPH <http://minsegpres.cl/grafo> {")
    arguments = ['<http://minsegpres.cl/funcionario#<<id>>> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/estamento> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/apellidoPaterno> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/apellidoMaterno> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://xmlns.com/foaf/0.1/givenName> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/grado> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/formacion> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/cargo> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/region> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/asignacionesExtras> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/unidadMonetaria> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/remuBruta> "<<data>>"^^xsd:integer .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/horasExtraordinarias> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/cometidosFuncionarios> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/fechaInicio> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/fechaTermino> "<<data>>" .',
                 '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/observaciones> "<<data>>" .'
                ]
    arguments_extra = ['<http://minsegpres.cl/horas_extraordinarias#<<id>>> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://transparencia.cl/horas_extraordinarias> .',
                 '<http://minsegpres.cl/horas_extraordinarias#<<id>>> <http://transparencia.cl/voc/horas_extraordinarias/mes> "<<data>>" .',
                 '<http://minsegpres.cl/horas_extraordinarias#<<id>>> <http://transparencia.cl/voc/horas_extraordinarias_diurnas/numero> "<<data>>"^^xsd:integer .',
                 '<http://minsegpres.cl/horas_extraordinarias#<<id>>> <http://transparencia.cl/voc/horas_extraordinarias_diurnas/unidadMonetaria> "<<data>>" .',
                 '<http://minsegpres.cl/horas_extraordinarias#<<id>>> <http://transparencia.cl/voc/horas_extraordinarias_diurnas/valorTotal> "<<data>>"^^xsd:integer .',
                 '<http://minsegpres.cl/horas_extraordinarias#<<id>>> <http://transparencia.cl/voc/horas_extraordinarias_nocturnas/numero> "<<data>>"^^xsd:integer .',
                 '<http://minsegpres.cl/horas_extraordinarias#<<id>>> <http://transparencia.cl/voc/horas_extraordinarias_nocturnas/unidadMonetaria> "<<data>>" .',
                 '<http://minsegpres.cl/horas_extraordinarias#<<id>>> <http://transparencia.cl/voc/horas_extraordinarias_nocturnas/valorTotal> "<<data>>"^^xsd:integer .'
                ]
    arguments_viaticos = ['<http://minsegpres.cl/viaticos#<<id>>> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://minsegpres.cl/viaticos> .',
                 '<http://minsegpres.cl/viaticos#<<id>>> <http://transparencia.cl/voc/viaticos/mes> "<<data>>" .',
                 '<http://minsegpres.cl/viaticos#<<id>>> <http://transparencia.cl/voc/viaticos/fecha> "<<data>>" .',
                 '<http://minsegpres.cl/viaticos#<<id>>> <http://transparencia.cl/voc/viaticos/lugar> "<<data>>" .',
                 '<http://minsegpres.cl/viaticos#<<id>>> <http://transparencia.cl/voc/viaticos/unidadMonetaria> "<<data>>" .',
                 '<http://minsegpres.cl/viaticos#<<id>>> <http://transparencia.cl/voc/viaticos/valor> "<<data>>"^^xsd:integer .'
                ]
    #print headers
    numero_funcionario = 0
    numero_viatico = 0
    numero_horas_extra = 0
    for item in page.xpath("//table[@class='tabla']/tbody/tr"):
        counter = 1
        sys.stdout.write(arguments[0].replace("<<id>>", numero_funcionario.__str__()))
        dpt = '<http://minsegpres.cl/funcionario#<<id>>> <http://purl.org/dc/terms/source> <http://www.minsegpres.gob.cl> .'
        sys.stdout.write(dpt.replace("<<id>>", numero_funcionario.__str__()))
        dpt = '<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/trabaja_en> "minsegpres" .'
        sys.stdout.write(dpt.replace("<<id>>", numero_funcionario.__str__()))
        for item2 in item.xpath("td"):
            target = arguments[counter].replace("<<id>>", numero_funcionario.__str__())
            #print etree.tostring(item2)
            valid = True
            if((item2.text is not None)):
                if(item2.text.strip() == ""):
                    valid = False
                    target = target.replace("<<data>>", "")
                else:
                    target = target.replace("<<data>>", item2.text.strip())
                    target = target.replace("(","")
                    target = target.replace("\n",", ")
                    target = target.replace(")","")
            else:
                empty = True
                for item3 in item2.xpath("a"):
                    empty = False
                    target = target.replace("<<data>>", item3.text.strip())

                    ##if it founds an item...
                    comparer = item3.text.strip()
                    if(comparer == "Si"):
                        #print url+"/"+item3.attrib["href"]
                        page2 = html.fromstring(urllib.urlopen("http://transparencia.minsegpres.gob.cl/PERSONAL/"+item3.attrib["href"]).read())
                        #if(page2.xpath("//table[@class='tabla']/tbody/tr/td")[0].text == "Total"):
                        #    print "AAHHGHGHAHGHSGHSDHGA"
                        #checker = page2.xpath("//table[@class='tabla']/tbody/tr")
                        #checker = checker[len(checker)-1].xpath("td")
                        for item_crawl in page2.xpath("//table[@class='tabla']/tbody/tr"):
                            target_crawl = ""
                            if "cometidos_funcionarios" in item3.attrib["href"]:
                                target_crawl = arguments_viaticos[0].replace("<<id>>", numero_viatico.__str__())
                            else:
                                target_crawl = arguments_extra[0].replace("<<id>>", numero_horas_extra.__str__())
                            sys.stdout.write(unicode(target_crawl))

                            thing_index = 1
                            for item_crawl2 in item_crawl.xpath("td"):

                                if "cometidos_funcionarios" in item3.attrib["href"]:
                                    target_crawl = arguments_viaticos[thing_index].replace("<<id>>", numero_viatico.__str__())
                                else:
                                    target_crawl = arguments_extra[thing_index].replace("<<id>>", numero_horas_extra.__str__())
                                content = item_crawl2.text.strip()
                                if("valor" in target_crawl):
                                    content = content.__str__().replace(".", "")
                                target_crawl = target_crawl.replace("<<data>>", content.__str__())

                                sys.stdout.write(unicode(target_crawl))
                                thing_index = thing_index + 1
                            string_extra = "<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/hasBono> <http://minsegpres.cl/horas_extraordinarias#<<id2>>> ."
                            string_viatico = "<http://minsegpres.cl/funcionario#<<id>>> <http://transparencia.cl/voc/hasBono> <http://minsegpres.cl/viaticos#<<id2>>> ."
                            if "cometidos_funcionarios" in item3.attrib["href"]:
                                string_viatico = string_viatico.replace("<<id>>", numero_funcionario.__str__())
                                string_viatico = string_viatico.replace("<<id2>>", numero_viatico.__str__())
                                sys.stdout.write(string_viatico)
                                numero_viatico = numero_viatico + 1
                            else:
                                string_extra = string_extra.replace("<<id>>", numero_funcionario.__str__())
                                string_extra = string_extra.replace("<<id2>>", numero_horas_extra.__str__())
                                sys.stdout.write(string_extra)
                                numero_horas_extra = numero_horas_extra + 1


                if(empty):
                    target = target.replace("<<data>>", "")
            if valid:
                sys.stdout.write( unicode(target))
            counter = counter + 1
        numero_funcionario = numero_funcionario + 1
    print "} }"













#############

#main_process("http://transparenciaactiva.minsegpres.cl/2015/per_planta.html")

main_process("http://transparencia.minsegpres.gob.cl/PERSONAL/dotacionplanta_periodo.asp?periodo=10&mes=492")
