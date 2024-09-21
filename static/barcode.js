var barcode = "";
var interval;
document.addEventListener('keydown', function(evt) {
    if(interval){
        clearInterval(interval);
    }
    if(evt.code == "Enter"){
        if(barcode){
            handleBarcode(barcode);
        }
        barcode = '';
        return;
    }
    if(evt.key != "Shift"){
        barcode += evt.key;
    }
    interval = setInterval(()=> barcode = "", 20);
    function handleBarcode(scanned_barcode){
        console.log(scanned_barcode);
        document.querySelector("#barcodeDisplay").innerHTML = scanned_barcode;
        let form_doc = document.querySelector("#barcodeValue");
        form_doc.value = scanned_barcode;
        form_doc.form.submit();
        barcode = "";
    }
});