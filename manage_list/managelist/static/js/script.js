$(document).ready(()=>{
    var preid="#itembtn1";
    $("#btn1").addClass('add-color')
    var btn_id="#btn1"
    function showitem(itemid,btn_id){
        $(itemid).addClass('d-block')
        $(itemid).removeClass('d-none')
        $(btn_id).addClass('add-color')
    }
    function removeitem(preid,btn_id){
        $(preid).addClass('d-none')
        $(preid).removeClass('d-block')
        $(btn_id).removeClass('add-color')
    }
   
    $(".showitem").click((ele)=>{
        removeitem(preid,btn_id)
        let id=ele.target.id
        btn_id="#"+id
        let itemid="#item"+id
        preid="#item"+id
        showitem(itemid,btn_id)
        
    })
})