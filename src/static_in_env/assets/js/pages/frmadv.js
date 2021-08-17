$(function() {
    $('#reportrange').daterangepicker({
        autoUpdateInput: true,
    })
});

function copy() {
    var n1 = document.getElementById("test1");
    var n2 = document.getElementById("test2");
    var n3 = document.getElementById("date1");
    var n4 = document.getElementById("date2");
    n3.value = n1.value;
    n4.value = n2.value;
}