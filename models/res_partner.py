# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, SUPERUSER_ID, _
import datetime

class Partner(models.Model):
    _inherit = "res.partner"

    estado_civil = fields.Selection([('soltero', 'Soltero(a)'),
            ('casado', 'Casado (o similar)'),
            ('viudo', 'Viudo(a)'),
            ('divorciado', 'Divorciado')])
    nacionalidad = fields.Many2one('res.country','Nacionalidad')
    # profersion = fields.Char('Profesión')
    dpi = fields.Char('DPI')
    fecha_nacimiento = fields.Date('Fecha nacimiento')
    edad = fields.Integer(compute='_get_edad',string='Edad')
    direccion_correspondencia = fields.Char('Direccion de correspondencia')

    def _get_edad(self):
        for partner in self:
            if partner.fecha_nacimiento:
                dia_nacimiento = int(datetime.datetime.strptime(str(partner.fecha_nacimiento),'%Y-%m-%d').date().strftime('%d'))
                mes_nacimiento = int(datetime.datetime.strptime(str(partner.fecha_nacimiento),'%Y-%m-%d').date().strftime('%m'))
                anio_nacimiento = int(datetime.datetime.strptime(str(partner.fecha_nacimiento),'%Y-%m-%d').date().strftime('%Y'))
                dia_actual = int(datetime.date.today().strftime('%d'))
                mes_actual = int(datetime.date.today().strftime('%m'))
                anio_actual = int(datetime.date.today().strftime('%Y'))

                resta_dia = dia_actual - dia_nacimiento
                resta_mes = mes_actual - mes_nacimiento
                resta_anio = anio_actual - anio_nacimiento

                if (resta_mes < 0):
                    resta_anio = resta_anio - 1
                elif (resta_mes == 0):
                    if (resta_dia < 0):
                        resta_anio = resta_anio - 1
                    if (resta_dia > 0):
                        resta_anio = resta_anio
                partner.edad = resta_anio
