# Copyright (c) 2025, José Maia de Oliveira and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from appointment_scheduler.utils.end_date_calculator import calculate_end_datetime

class Appointment(Document):
    def before_save(self):
        self.end_date = calculate_end_datetime(self.start_date, self.duration)

        appointments_has_conflict = frappe.db.sql("""
            SELECT name
            FROM `tabAppointment`
            WHERE seller = %s
            AND name != %s
            AND start_date < %s
            AND end_date > %s
        """, (self.seller, self.name, self.end_date, self.start_date), as_dict=True)

        if appointments_has_conflict:
            frappe.throw("O vendedor já possui um compromisso nesse intervalo de tempo.")


