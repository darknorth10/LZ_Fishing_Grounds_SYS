$(document).ready(function () {
    
    // open modal per item
    $(document).on("click", ".product_group", function () {
        
        let id = $(this).attr("data-id");

        $("#product_id").val(id);
        $("#openQuantityModal").click();
        
    });

    // add item to cart
    $("#addQuantityForm").submit(function (e) { 
        e.preventDefault();

        var xhref = $.ajax({
            type: "post",
            url: location.href,
            data: $(this).serialize(),
            
            success: function (response) {

                if (response.success) {
                    console.log(response)
                    $("#cart").load(location.href+" #cart>*","");
                    $("#ConfirmationForm").load(location.href+" #ConfirmationForm>*","");
                    $("#dialogDeleteClose").click();
                    $("#qtty").val("");
                } else {
                    alert(response.err)
                }
                
            }
        });

        
    });

    // delete item
    $(document).on("click", ".delbtn", function () {
        
        let itemID = $(this).attr("data-id");
        
        console.log(itemID)
        // $("#total").text( $("#subtotaltxt").text() );

        $("#delItem").attr("href", itemID);

        $("#opendialogDelete").click();

    });

    $("#delItem").click( function(e) {
        e.preventDefault();

        window.location.href = $(this).attr('href');
        
        
    });


    $(document).on("click", "#proceedBtn", function (e) { 
        // $("#total").text( $(document).find("#subtotaltxt").text() );
        $("#openConfirmationModal").click();
        
    });


    $(document).on('change', "input:radio[name='payment_type']", function () {
        console.log("asdasd")
    });
});