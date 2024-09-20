import os
from xml.etree import ElementTree as ET

from flask import Blueprint, jsonify, request
from models.lenguaje import Lenguaje

BlueprintLenguaje = Blueprint('lenguaje', __name__)

@BlueprintLenguaje.route('/lenguaje/cargar', methods=['POST'])
def cargar_Lenguajes():
    try:
        lenguajes = []
        xml_entrada = request.data.decode('utf-8')
        if xml_entrada == '':
            return jsonify({
                'mensaje': 'No se ha enviado un XML',
                'status': 404
                }),404
        xml_entrada = xml_entrada.replace('\n', '')
        root = ET.fromstring(xml_entrada)
        for lenguaje in root:
            nombre = ''
            popularidad = ''
            uso = ''
            usuarios = ''
            logo = ''
            for caracteristica in lenguaje:
                if caracteristica.tag == 'nombre':
                    nombre = caracteristica.text
                if caracteristica.tag == 'popularidad':
                    popularidad = caracteristica.text
                if caracteristica.tag == 'uso':
                    uso = caracteristica.text
                if caracteristica.tag == 'usuarios':
                    usuarios = caracteristica.text
                if caracteristica.tag == 'logo':
                    logo = caracteristica.text
            lenguaje = Lenguaje(nombre, popularidad, uso, usuarios, logo)
            lenguajes.append(lenguaje)
            if os.path.exists('database/lenguajes.xml'):
                tree = ET.parse('database/lenguajes.xml')
                root = tree.getroot()
                nuevo_lenguaje = ET.SubElement(root, 'lenguaje')
                nombre = ET.SubElement(nuevo_lenguaje, 'nombre')
                nombre.text = lenguaje.getNombre()
                popularidad = ET.SubElement(nuevo_lenguaje, 'popularidad')
                popularidad.text = lenguaje.getPopularidad()
                uso = ET.SubElement(nuevo_lenguaje, 'uso')
                uso.text = lenguaje.getUso()
                usuarios = ET.SubElement(nuevo_lenguaje, 'usuarios')
                usuarios.text = lenguaje.getUsuarios()
                logo = ET.SubElement(nuevo_lenguaje, 'logo')
                logo.text = lenguaje.getLogo()
                tree.append(nuevo_lenguaje)
                ET.indent(tree, space='\t', level=0)
                tree.write('database/lenguajes.xml', encoding='utf-8', xml_declaration=True)
        #SI EN DADO CASO NO EXISTE EL XML, LO CREAMOS
        if not os.path.exists('database/lenguajes.xml'):
            with open('database/lenguajes.xml', 'w', encoding='utf-8') as file:
                file.write(xml_entrada)
                file.close()
        
        return jsonify({
            'message': 'Archivo cargado correctamente',
            'status': 200
        }), 200
    except:
        return jsonify({
            'message': 'Error al cargar el xml',
            'status': 500
        }), 500
    
@BlueprintLenguaje.route('/lenguaje/verLenguajes', methods=['GET'])
def obtenerLenguajes():
    lenguajes = precargarLenguajes()
    diccionario_salida = {
        'mensaje': 'Lenguajes encontrados',
        'lenguajes':[],
        'status': 200
    }
    for lenguaje in lenguajes:
        diccionario_salida['lenguajes'].append({
            'nombre': lenguaje.getNombre(),
            'popularidad': lenguaje.getPopularidad(),
            'uso': lenguaje.getUso(),
            'usuarios': lenguaje.getUsuarios(),
            'logo': lenguaje.getLogo()
        })
    return jsonify(diccionario_salida), 200

def precargarLenguajes():
    lenguajes = []
    if os.path.exists('database/lenguajes.xml'):
        tree = ET.parse('database/lenguajes.xml')
        root = tree.getroot()
        for lenguaje in root:
            nombre = ''
            popularidad = ''
            uso = ''
            usuarios = ''
            logo = ''
            for caracteristica in lenguaje:
                if caracteristica.tag == 'nombre':
                    nombre = caracteristica.text
                if caracteristica.tag == 'popularidad':
                    popularidad = caracteristica.text
                if caracteristica.tag == 'uso':
                    uso = caracteristica.text
                if caracteristica.tag == 'usuarios':
                    usuarios = caracteristica.text
                if caracteristica.tag == 'logo':
                    logo = caracteristica.text
            lenguajes.append(Lenguaje(nombre, popularidad, uso, usuarios, logo))
    return lenguajes