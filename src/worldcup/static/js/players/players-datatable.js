$(document).ready(function() {
  // Datatable
  var myDataTable = $('#players-table').DataTable({
    "iDisplayLength": 12,
    "order": [[ 2, "asc" ]],
    "lengthMenu": [[12, 23, 46, 92, 184, -1], [12, 23, 46, 92, 184, "All"]],
    "sDom": '<"top">rt<"bottom"lp><"clear">'
  });

  // Custom search box
  $('#myPlayerSearchBox').keyup(function(){
    myDataTable.search($(this).val()).draw() ;
  })
});