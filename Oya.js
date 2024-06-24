const mobile = document.querySelector('menu-toggle');
const mobileLink = document.querySelector('.sidebar');

mobile.addEventListener("click", function(){
    mobile.cleanList.toggle("is-active");
    mobileLink.cleanList.toggle("active");

})

mobileLink.addEventListener("click", function(){
    const menullars = document.querySelector("is-active");
    if(window-innerwidth<=768 &&  menullars){
        mobile.classList.toggle("is-active");
        mobileLink.classList.toggle("active");
    }
})

var step=100;
var stepfilter = 60;
var scrolling = true;

s(".back").bind("click", function(e){
    e.preventDefault();
    s("highlight-wrapper").animate({
        scrollLeft: "-="+ step + "px"
    });
});

s(".next").bind("click", function(e){
    e.preventDefault();
    s("highlight-wrapper").animate({
        scrollLeft: "+="+ step + "px"
    });
});

s(".back-menus").bind("click", function(e){
    e.preventDefault();
    s("filter-wrapper").animate({
        scrollLeft: "-="+ stepFilter + "px"
    });
});

s(".next-menus").bind("click", function(e){
    e.preventDefault();
    s("filter-wrapper").animate({
        scrollLeft: "+="+ steFilter + "px"
    });
});



