// $(()=>{
// 	$('#submitform').click(()=>{

// 		let location = $('#location').val()
// 		let incident_des = $('#incident_des').val()
// 		let incident_date = $('#incident_date').val()
// 		let incident_time = $('#incident_time').val()
// 		let incident_location = $('#incident_location').val()
// 		let incident_severity = $('#incident_severity').val()
// 		let suspected_cause = $('#suspected_cause').val()
// 		let action_taken = $('#action_taken').val()
// 		let list_of_subtype = []
// 		let reported_by = $('#reported_by').val()
// 		let csrfToken = $('input[name=csrfmiddlewaretoken]').val()

		
// 		$.each($("input[name='sub_incident_types']:checked"), function(){
// 			list_of_subtype.push($(this).val());
// 		});

// 		data = {location:location, incident_des:incident_des, incident_date:incident_date,
// 			incident_time:incident_time, incident_location:incident_location, incident_severity:incident_severity,
// 			suspected_cause:suspected_cause, action_taken:action_taken, list_of_subtype:list_of_subtype,
// 			reported_by:reported_by}


// 			if(location=='' || incident_des=='' || incident_date=='' || incident_time==''||
// 				incident_location=='' || incident_severity=='' || suspected_cause=="" || action_taken=='' || list_of_subtype==''
// 				|| reported_by==''){

// 				alert('Please Fill All the information')

// 		}else{
// 			console.log(data)

// 			$.ajax({
// 				headers: {
// 					'X-CSRFToken' : csrfToken
// 				},
// 				url : "{% url 'app:incidentprocess' %}",
// 				type: 'POST',
// 				success:()=>{
// 					console.log('Sccuess')
// 				},
// 				fail:()=>{
// 					console.log('Fail')
// 				}

// 			})


// 		}

		
// 	})
// })