const item_form=document.getElementById("item-form")
let add_btn=document.getElementById("add_item")
console.log(add_btn)
add_btn.addEventListener("click",()=>{
    let clone_node=item_form.cloneNode(true)
    console.log(clone_node)
        let cust_form=document.getElementById("cust_form")
    let subBtn=document.getElementById("submit")
    subBtn.remove()
    add_btn.remove()
    cust_form.appendChild(clone_node)
    cust_form.appendChild(subBtn)
    cust_form.appendChild(add_btn)
    let ele=document.getElementsByClassName("myitem")
    console.log(ele)
    for(let e=ele.length-3;e<ele.length;e++)
    {
    ele[e].value=""
    }
})