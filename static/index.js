const item_form=document.getElementById("item-form")
let add_btn=document.getElementById("add_item")
let sub_btn=document.getElementById("sub_btn")
let add_sub_btn=document.getElementById("add/submit")   

let itemHelp=document.getElementById("itemHelp")
let priceHelp=document.getElementById("priceHelp")
let nameHelp=document.getElementById("nameHelp")
let phoneHelp=document.getElementById("phoneHelp")

let req_field=`<i class="fa fa-exclamation-triangle text-danger">This field is required</i>`

function clearWarnings()
{
itemHelp.innerHTML=""

priceHelp.innerHTML=""

nameHelp.innerHTML=""

phoneHelp.innerHTML=""
return
}

let form = document.getElementById("cust_form");
function handleForm(event) { event.preventDefault(); } 

add_btn.addEventListener("click",()=>{
    let itemname=document.getElementsByName('itemname')[0].value
let price=document.getElementsByName("price")[0].value
    if (itemname=="")
    {   itemHelp.innerHTML=req_field
        return
    }
    if (price=="")
    {
        priceHelp.innerHTML=req_field
        return 
    }

    let clone_node=item_form.cloneNode(true)
        let cust_form=document.getElementById("cust_form")
    add_sub_btn.remove()
    cust_form.appendChild(clone_node)
    cust_form.appendChild(add_sub_btn)
    let ele=document.getElementsByClassName("myitem")
    for(let e=ele.length-3;e<ele.length;e++)
    {
    ele[e].value=""
    }
})
sub_btn.addEventListener("click",()=>{
    form.addEventListener('submit', handleForm);
let itemname=document.getElementsByName('itemname')[0].value
let price=document.getElementsByName("price")[0].value
let naame=document.getElementsByName("name")[0].value
let phone=document.getElementsByName("phone")[0].value

    clearWarnings()
    if (itemname=="")
    {   
        itemHelp.innerHTML=req_field
        return
    }
    if (price=="")
    {           
        priceHelp.innerHTML=req_field
    return }

if (naame=="")
    {        nameHelp.innerHTML=req_field
        return
    }
    if (phone=="")
    {        phoneHelp.innerHTML=req_field

    return 
    }

form.removeEventListener('submit',handleForm)
document.myform.action="succeed/"
})