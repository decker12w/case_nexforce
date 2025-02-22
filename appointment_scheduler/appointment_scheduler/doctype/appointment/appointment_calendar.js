frappe.views.calendar["Appointment"] = {
	field_map: {
		start: "start_date",
		end: "end_date",
		id: "name",
		allDay: "all_day",
		title: "client_name",
	},
	order_by: "start_date",
	get_events_method: "appointment_scheduler.appointment_scheduler.events.get_events",
	get_css_class: function (data) {
		switch (data.status) {
			case "Scheduled":
				return "warning";
			case "Finished":
				return "success";
			case "Canceled":
				return "danger";
			default:
				return "info";
		}
	},
};
