$.ctrl = function(key, callback, args) {
    $(document).keydown(function(e) {
        if(!args) args=[]; // IE barks when args is null 
        console.log(e.keyCode)
        if((e.keyCode == key.charCodeAt(0) || e.keyCode == key) && e.ctrlKey) {
            callback.apply(this, args);
            return false;
        }
    });        
};
$.shortcut = function(key, callback, args) {
    $(document).keydown(function(e) {
        if(!args) args=[]; // IE barks when args is null
        console.log(e.keyCode)
        if((e.keyCode == key.charCodeAt(0) || e.keyCode == key)) {
            callback.apply(this, args);
            return false;
        }
    });
};
//New object by Ctrl + enter
$.ctrl('13', function() {
	$('.oe_form_button_create').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
		}
	});
	$('.oe_list_add').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
		}
	});
});
//Edit the current object F2
$.shortcut('113', function() {
	$('.oe_form_button_edit').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
		}
	});
});
//Save the current object
$.ctrl('S', function() {

	var ok= true;
	$('.oe_abstractformpopup-form-save').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
			ok = false
		}
	});
	if(ok){
		$('.oe_form_button_save').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
		}
	});
	}

});
//Save current pop-up and open new one ctrl+espace
$.ctrl('32', function() {

	$('.oe_abstractformpopup-form-save-new').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
			ok = false
		}
	});
});
//Cancel the current object edition
$.ctrl('Z', function() {
	$('.oe_form_button_cancel').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
		}
	});
});

//Delete the current object
$.ctrl('190', function() {
	$("a:contains('Delete')").each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).click();
		}
	});
	$("a:contains('Supprimer')").each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).click();
		}
	});
});
$.ctrl('46', function() {
	$("a:contains('Delete')").each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).click();
		}
	});
	$("a:contains('Supprimer')").each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).click();
		}
	});
});
//add item ctrl +
//add item ctrl +
$.ctrl('107', function() {
	$("td.oe_form_field_one2many_list_row_add a").each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).click();
		}
	});
	$("td.oe_form_field_many2many_list_row_add a").each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).click();
		}
	});

});
//remove item ctrl -
$.ctrl('109', function() {
	$("td.oe_form_field_one2many_list_row_add").parent().prev().children('.oe_list_record_delete').children('button.oe_i').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).click();
		}
	});
	$("td.oe_form_field_many2many_list_row_add").parent().prev().children('.oe_list_record_delete').children('button.oe_i').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).click();
		}
	});
});
//Duplicate the current object
$.ctrl('D', function() {
	$("a:contains('Duplicate')").each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).click();
		}
	});
	$("a:contains('Dupliquer')").each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).click();
		}
	});
});

//Previous object
$.shortcut('33', function() {
	$('.oe_i[data-pager-action="previous"]').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
		}
	});
});
//Next object
$.shortcut('34', function() {
	$('.oe_i[data-pager-action="next"]').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
		}
	});
});
//update
$.shortcut('112', function() {
	$('.oe_subtotal_footer_separator button.oe_button.oe_form_button.oe_edit_only.oe_link').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
		}
	});
	$("span:contains('(update)')").each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).parents('.oe_button.oe_form_button.oe_link.oe_edit_only').trigger('click');
		}

	});
	$("span:contains('(mise à jour)')").each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).parents('.oe_button.oe_form_button.oe_link.oe_edit_only').trigger('click');
		}

	});
});