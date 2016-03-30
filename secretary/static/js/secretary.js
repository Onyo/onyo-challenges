function delete_contact(row){
	if (confirm("Do you want delete this contact?") == true) {
        tr = $(row).parent().parent();
		id = $(tr).find(".id").text()
		url = SERVER_URL + "/contacts/" + id;
		$.ajax({
		    type: "DELETE",
		    url: url,
		    success: function(response){
		    	$("tr[data-id="+id+"]").remove();						      
		    },
		    error: function(response){
		      console.log(response.responseText);
		    },
		    dataType: "json"
		});	  					
    } 
}

function clear_form(){
	$("#postcode").val("");
	$("#number").val("");
	$("#name").val("");
	$("#address").val("");
	$("#id").val("");	
	$("tr").removeClass("success");
	$("tr").removeClass("active");	
}

function edit_contact(row){
	tr = $(row).parent().parent();
	$("#postcode").val($(tr).find(".postcode").text());
	$("#name").val($(tr).find(".name").text());	
	$("#number").val($(tr).find(".number").text());	
	$("#address").val($(tr).find(".address").text());	
	$("#id").val($(tr).find(".id").text());	
	$("#method-button").val("PUT");
	$(tr).attr("class", "active");
	$("tr").removeClass("success");
}

function make_request(){
	url = SERVER_URL + "/contacts";
	postcode = $("#postcode").val();
	data = {"postcode": postcode, "name": $("#name").val(), "number": $("#number").val()};
	id = $("#id").val();
	if(id){
		url += "/" + id;
	}

	method = $("#method-button").val();
	$.ajax({
	    type: method,
	    url: url,
	    data: data,
	    success: function(response){
	    	clear_form();
	    	//Verifies with is a new contact or updated one
	    	html = "<tr class='success' data-id='"+response['id']+"'><td class='id'>"+response['id']+"</td><td class='name'>"+response['name']+"</td><td class='postcode'>"+response['postcode']+"</td><td class='number'>"+response['number']+"</td><td><span class='address'>"+response['address']+"</span><button type='button' class='btn btn-xs btn-danger' style='float:right;' onclick='delete_contact(this)'>Delete</button><button type='button' class='btn btn-xs btn-primary' style='float:right;margin-right: 5px;' onclick='edit_contact(this)'>Edit</button></td></tr>";

	    	tr = $("tr[data-id="+response['id']+"]");
	    	if(tr.length > 0){
	    		tr.replaceWith(html);
	    	}else{
		      $(".list").append(html);	
	    	}
			
	    },
	    error: function(response){
	      console.log(response.responseText);
	    },
	    dataType: "json"
	});	    			
}