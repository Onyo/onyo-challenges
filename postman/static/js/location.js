function delete_location(row){
	if (confirm("Do you want delete this location?") == true) {
        tr = $(row).parent().parent();
		postcode = $(tr).find(".postcode").text()
		url = SERVER_URL + "/locations/" + postcode;
		$.ajax({
		    type: "DELETE",
		    url: url,
		    success: function(response){
		    	$("tr[data-postcode="+postcode+"]").remove();						      
		    },
		    error: function(response){
		      console.log(response.responseText);
		    },
		    dataType: "json"
		});	  					
    } 
}

function edit_location(row){
	tr = $(row).parent().parent();
	$("#postcode").val($(tr).find(".postcode").text());
	$("#postcode").attr("readonly", "true");
	$("#address").val($(tr).find(".address").text());	
	$("#id").val($(tr).find(".id").text());	
	$("#method-button").val("PUT");
	$(tr).attr("class", "active");
	$("tr").removeClass("success");
}

function clear_form(){
	console.log("clear");
	$("#postcode").val("");
  	$("#address").val("");
  	$("#postcode").removeAttr("readonly");
	$("tr").removeClass("success");
	$("tr").removeClass("active");	  	
}

function make_request(){
	url = SERVER_URL + "/locations";
	postcode = $("#postcode").val();
	data = {"postcode": postcode, "address": $("#address").val()};
	id = $("#id").val();
	if(id){
		url += "/" + postcode;
	}

	method = $("#method-button").val();
	$.ajax({
	    type: method,
	    url: url,
	    data: data,
	    success: function(response){
	    	clear_form();

	    	//Verifies with is a new location or updated one
	    	html = "<tr class='success' data-postcode='"+response['postcode']+"'><td class='id'>"+response['id']+"</td><td class='postcode'>"+response['postcode']+"</td><td><span class='address'>"+response['address']+"</span><button type='button' class='btn btn-xs btn-danger' style='float:right;' onclick='delete_location(this)'>Delete</button><button type='button' class='btn btn-xs btn-primary' style='float:right;margin-right: 5px;' onclick='edit_location(this)'>Edit</button></td></tr>";

	    	tr = $("tr[data-postcode="+response['postcode']+"]");
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