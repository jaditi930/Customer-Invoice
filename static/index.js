const item_form=document.getElementById("item-form")
let add_btn=document.getElementById("add_item")
let sub_btn=document.getElementById("sub_btn")
let add_sub_btn=document.getElementById("add/submit")   

add_btn.addEventListener("click",()=>{
    let itemname=document.getElementsByName('itemname')[0].value
    let price=document.getElementsByName("price")[0].value
    if (itemname=="")
    {   document.getElementById("itemHelp").innerHTML=`<i class="fa fa-exclamation-triangle"></i>`
    document.getElementById("itemHelp").innerText="This Field is required"
        return}
    if (price=="")
    {
        document.getElementById("priceHelp").innerHTML=`<i class="fa fa-exclamation-triangle"></i>`
        document.getElementById("priceHelp").innerText="This Field is required"
    return }

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
    console.log("Excecuting")
    let itemname=document.getElementsByName('itemname')[0].value
    let price=document.getElementsByName("price")[0].value
    console.log(itemname,price)
    if (itemname=="")
    {   
        document.getElementById("itemHelp").innerHTML=`<i class="fa fa-exclamation-triangle"></i>`
        document.getElementById("itemHelp").innerText="This Field is required"
        return}
    if (price=="")
    {           
        document.getElementById("priceHelp").innerHTML=`<i class="fa fa-exclamation-triangle"></i>`
        document.getElementById("priceHelp").innerText="This Field is required"
    return }
let name=document.getElementsByName("name")[0].value
let phone=document.getElementsByName("phone")[0].value
if (name=="")
    {        document.getElementById("nameHelp").innerHTML=`<i class="fa fa-exclamation-triangle"></i>`
        document.getElementById("nameHelp").innerText="This Field is required"
        return}
    if (phone=="")
    {        document.getElementById("phoneHelp").innerHTML=`<i class="fa fa-exclamation-triangle"></i>`

        document.getElementById("phoneHelp").innerText="This Field is required"
    return }
    console.log("reached")
document.getElementsByName("myform")[0].action="succeed/"
 
})