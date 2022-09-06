(function($) {



  $("#btnExport_excel").click(function() {
    let today = new Date()

    var nameformat = today.toISOString().substring(0, 13)
      
    $('#table2excel').table2excel({
      // exclude CSS class
      exclude: ".excludeThisClass",
      name: "Worksheet Name",
      filename: "student_list_" + nameformat, //do not include extension
      fileext: ".xlsx" // file extension
      }); 

  });


  $("#btnExport_excel_fees").click(function() {
    let today = new Date()

    var nameformat = today.toISOString().substring(0, 13)
      
    $('#table2excel_fees').table2excel({
      // exclude CSS class
      exclude: ".excludeThisClass",
      name: "Worksheet Name",
      filename: "receipt_list_" + nameformat, //do not include extension
      fileext: ".xlsx" // file extension
      }); 

  });


  $("#btnExport_excel_staff").click(function() {
    let today = new Date()

    var nameformat = today.toISOString().substring(0, 13)
      
    $('#table2excel_staff').table2excel({
      // exclude CSS class
      exclude: ".excludeThisClass",
      name: "Worksheet Name",
      filename: "staff_list_" + nameformat, //do not include extension
      fileext: ".xlsx" // file extension
      }); 

  });


  $("#btnExport_pdf").click(function() {
    var pdf = new jsPDF('p', 'pt', 'letter');
    // source can be HTML-formatted string, or a reference
    // to an actual DOM element from which the text will be scraped.
    source = $('#student_table_div')[0];

    cln_source2 = source.cloneNode(true);
    var deleterows = [];
    $(cln_source2.childNodes[1].rows).each(function(ri, row){
        var deletecells = [];
        $(row.cells).each(function(ci, cell){
            if( $(cell).hasClass('excludeThisClass') )
                deletecells.push(ci);
        });
        $.each(deletecells.reverse(), function(i, ii){
            row.deleteCell(ii);
        });

    });
    $.each(deleterows.reverse(), function(i, ii){
        cln_source2.childNodes[1].deleteRow(ii);
    });


    // we support special element handlers. Register them with jQuery-style 
    // ID selector for either ID or node name. ("#iAmID", "div", "span" etc.)
    // There is no support for any other type of selectors 
    // (class, of compound) at this time.
    specialElementHandlers = {
        // element with id of "bypass" - jQuery style selector
        '.excludeThisClass': function (element, renderer) {
            // true = "handled elsewhere, bypass text extraction"
            return true
        }
    };
    margins = {  
      top: 150,  
      bottom: 60,  
      left: 40,  
      right: 40,  
      width: 600  
  }; 
    // all coords and widths are in jsPDF instance's declared units
    // 'inches' in this case

/*     pdf.fromHTML(
        cln_source2, // HTML string or DOM elem ref.
        margins.left, // x coord
        margins.top, { // y coord
            'width': margins.width, // max width of content on PDF
            'elementHandlers': specialElementHandlers
        },

        function (dispose) {
            // dispose: object with X, Y of the last line add to the PDF 
            //          this allow the insertion of new lines after html
            pdf.save('Test.pdf');
        }, margins
    ); */

    const table = document.querySelector('table')

    var columns = []

    var data = []


    for (var i = 0, row; row = table.rows[i]; i++) {
      var arrayData = []
      //iterate through rows
      //rows would be accessed using the "row" variable assigned in the for loop
      for (var j = 0; j < 5 ; j++) {
        
        var col = row.cells[j]
        if(i == 0) {
          columns.push(col.innerHTML)
        }else{
          arrayData.push(col.innerHTML)
        }
        //console.log(col.innerHTML);
      }  

      if(arrayData.length > 0){
        data.push(arrayData)
      }
   }




    pageHeight = pdf.internal.pageSize.height; 
    

    var y = 5;
    pdf.setLineWidth(10);
    pdf.text(50, y = y + 20, "Student List");
    

    pdf.autoTable(columns,data,{
      startY: false,
      theme: 'plain',
      tableWidth: '500',
      columnWidth: 'wrap',
      showHead: 'everyPage',
      tableLineColor: 200,
      tableLineWidth: 0,
      columnStyles: {
          0: {
            cellWidth: 100
          },
          1: {
            cellWidth: 100
          },
          2: {
            cellWidth: 100
          },
          3: {
            cellWidth: 100
          },
          4: {
            cellWidth: 100
          },
          5: {
            cellWidth: 100
          },
      },
      headStyles: {
          theme: 'grid'
      },
      styles: {
          overflow: 'linebreak',
          cellWidth: 'wrap',
          font: 'arial',
          fontSize: 12,
          cellPadding: 8,
          overflowColumns: 'linebreak'
      },
  }); 

  pdf.save('Test.pdf');


  });
  

  })(jQuery);