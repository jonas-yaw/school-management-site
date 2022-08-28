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
        top: 80,
        bottom: 60,
        left: 40,
        width: 522
    };
    // all coords and widths are in jsPDF instance's declared units
    // 'inches' in this case

    pdf.fromHTML(
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
    );
  });
  

  })(jQuery);