# -*- coding: utf-8 -*-


"""
redondeo y duración 
minima de un ticket 

"""

from odoo import models

from math import ceil


class PlanesentAcountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
   
    def write(self, vals):

        if "unit_amount" in vals:

            print("WRITE")
            minimum_duration = 0.25
            rounding = 0.50 
            minutes_spent = max(minimum_duration, vals["unit_amount"]) * 60
            if rounding and ceil(minutes_spent % rounding) != 0:
                minutes_spent = ceil(minutes_spent / rounding) * rounding
            vals["unit_amount"] = minutes_spent / 60
            
        super().write(vals)