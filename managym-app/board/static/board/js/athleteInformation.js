$('#save-injury').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget); // Button that triggered the modal
  var id = button.data('information-id'); // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  var modal = $(this);
  modal.find('.modal-title').text(id ? 'Edit injury' : 'New injury');
  modal.find('#type_information').val('injury');
  if (id) {
  	var body = $(button).parent().parent().find('.information-body').text();
  	modal.find('#id_body').val(body);
  	modal.find('#id_information').val(id);
  } else {
  	modal.find('#id_body').val('');
  	modal.find('#id_information').val('new');
  }
})

$('#save-comment').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget); // Button that triggered the modal
  var id = button.data('information-id'); // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  var modal = $(this);
  modal.find('.modal-title').text(id ? 'Edit comment' : 'New comment');
  modal.find('#type_information').val('comment');
  if (id) {
  	var body = $(button).parent().parent().find('.information-body').text();
  	modal.find('#id_body').val(body);
  	modal.find('#id_information').val(id)
  } else {
  	modal.find('#id_body').val('');
  	modal.find('#id_information').val('new');
  }
})
