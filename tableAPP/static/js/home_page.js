var tableData = ''
var row_id =''


$(document).ready(function(){
 $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".table tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });

   $(document).on("click",".table_dataSet tbody tr td button.btn-edit", function() { // any button
        row_id = "";
        row_id = $(this).attr('row_id');
        for(i = 0; i < tableData.length; ++i) {
            if (row_id == tableData[i]['id']){
            $('#as_id').val(tableData[i]['AmazonShipmentID'])
            $('#company_name').val(tableData[i]['CompanyName'])
            $('#date').val(tableData[i]['CreatedDate'])
            $('#pro_num').val(tableData[i]['PRONumber'])
            $('#ship_status').val(tableData[i]['ShipStatus'])
            $('#ss_num').val(tableData[i]['ShipStatusNum'])
            $('#total_cartons').val(tableData[i]['TotalCartons'])
            }

        }
    });

 $("#btn_update").click(function() {
       var pro_num = $('#pro_num').val();
       var c_name =  $('#company_name').val();
       var c_data =  $('#date').val();
       var a_ship =  $('#as_id').val();
       var total_car =  $('#total_cartons').val();
       var ship_s  =   $('#ship_status').val();
       var ss_num =    $('#ss_num').val();
       if ( (pro_num && c_data && c_name && a_ship && total_car && total_car && ship_s && ss_num) == ''){
         alert( 'Please fill the all fields')
       }
       else
       {
           var data = {}
           data['row_id'] = row_id;
           data['pro_num'] = pro_num;
           data['c_name'] = c_name;
           data['c_data'] = c_data;
           data['a_ship'] = a_ship;
           data['total_car'] = total_car;
           data['ship_s'] = ship_s;
           data['ss_num'] = ss_num;
           updateTableDataAPI(data);
       }
    });

     $(document).on("click",".table_dataSet tbody tr td button.btn-delete", function() { // any button
        row_id = "";
        row_id = $(this).attr('row_id');
        if (row_id == ""){
         alert('please select row')
        }
        else{
        var data = {}
        data['row_id'] = row_id;
        deleteTableDataAPI(data);
        }
    });
    LoadTableDataAPI();
});

function LoadTableDataAPI(){
data = "test"
$.ajax({
           url: "/api/tableData",
           type: "GET",
           contentType: 'application/json',
           data: JSON.stringify(data),
           success: function(data, testStatus, jqXHR){
           var table_data = data.data
           tableData = data.data
           renderNewsList(table_data)
           alert('data set from table successfully!')

           },
           error: function(response){
             alert("Error:" + response);
           }
        });
}

function updateTableDataAPI(data){
$.ajax({
           url: "/api/update",
           type: "POST",
           contentType: 'application/json',
           data: JSON.stringify(data),
           success: function(data, testStatus, jqXHR){
           var table_data = data.data
           tableData = data.data
           renderNewsList(table_data)
            $('#exampleModal').modal("hide");
           alert('data update table successfully!')

           },
           error: function(response){
             alert("Error:" + response);
           }
        });
}

function deleteTableDataAPI(data){
$.ajax({
           url: "/api/delete",
           type: "POST",
           contentType: 'application/json',
           data: JSON.stringify(data),
           success: function(data, testStatus, jqXHR){
           var table_data = data.data
           tableData = data.data
           renderNewsList(table_data)
           alert('data delete table successfully!')
           },
           error: function(response){
             alert("Error:" + response);
           }
        });
}



function renderNewsList(data){
     var data_view = $('.table_data');
     data_view.find('tr').remove();
       if (data.length > 0){
            var i;
            var sno = 0;
            for(i = 0; i < data.length; ++i) {
                 var clone = $('#template .table-form-list .table-row-form').clone();
                var sno = sno+1;
                $('.sno', clone).text(sno)
                $('.pro_num', clone).text(data[i]['PRONumber'])
                $('.c_name', clone).text(data[i]['CompanyName'])
                $('.c_data', clone).text(data[i]['CreatedDate'])
                $('.a_ship', clone).text(data[i]['AmazonShipmentID'])
                $('.ship_s', clone).text(data[i]['ShipStatus'])
                 $('.ship_sn', clone).text(data[i]['ShipStatusNum'])
                $('.total_car', clone).text(data[i]['TotalCartons'])
                var edit = '<button type="button"   data-toggle="modal" data-target="#exampleModal" class="btn btn-primary btn-edit" id="btn_edit" value="edit" row_id ="'+data[i]['id']+'">Edit</button>'
                var cancel = '<button type="button"  class="btn btn-danger btn-delete"  row_id ="'+data[i]['id']+'">Delete</button>'
                  $('.btn_edit', clone).append(edit)
                  $('.btn_cancel', clone).append(cancel)

                data_view.append(clone);
            }
       }
     else{
     $('.table_dataSet').hide();
     }
}




