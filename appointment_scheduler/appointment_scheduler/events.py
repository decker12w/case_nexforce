import frappe

@frappe.whitelist()
def get_events():
	data = frappe.db.sql("""
		SELECT *
		FROM `tabAppointment`
	""", as_dict=True)

	return data
