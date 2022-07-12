const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('nav a').forEach(link => {
  if(link.href.includes(`${activePage}`)){
    console.log(activePage);
    link.classList.add('active');

  }
})
const ColorChange=document.getElementById("logo1");

/*change the headeline backgroudn in bothpages*/
ColorChange.addEventListener("mouseover",function(){
  logo1.style.backgroundColor="Black";
  logo1.style.backgroundColor
  
},true);

ColorChange.addEventListener("mouseleave",function(){
  logo1.style.backgroundColor="#0082e6";
  
},true);




const getUser = () => {
    const formInputValue = document.getElementById("frontend-request").user_number.value;
    fetch(` https://reqres.in/api/users/${formInputValue}`)
        .then((response) => response.json())
        .then((object) => {
            const data = object?.data;
            document.getElementById("place_holder_for_response").innerHTML =
                `
                    <br>
                    <h3>${data?.first_name} ${data?.last_name}</h3>
                    <h4>${data?.email}</h4>
                    <img src="${data?.avatar}" alt="Profile Picture"/>
                `
        })
        .catch((err) => console.log(err));
}