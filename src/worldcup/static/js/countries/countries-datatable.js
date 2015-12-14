$(document).ready(function() {
  // Datatable
  var myDataTable = $('#countries-table').DataTable({
    "iDisplayLength": 10,
    "lengthMenu": [[3, 5, 10, 15, 20, -1], [3, 5, 10, 15, 20, "All"]],
    "sDom": '<"top">rt<"bottom"lp><"clear">'
  });

  // Custom search box
  $('#myCountrySearchBox').keyup(function(){
    myDataTable.search($(this).val()).draw() ;
  })
});