// [data-animation-scroll]
// [data-animation-scroll="cards-services-left"]
// [data-animation-scroll="cards-services-right"]
// [data-animation-scroll="cards-services-botton"]
// [data-animation-scroll].animate
const target = document.querySelectorAll('[data-animation-scroll]');
function animationScroll(){
const windownEixo_Y = window.pageYOffset + ((window.innerHeight * 3) / 4.4);
    target.forEach(function(e){
        if ( (windownEixo_Y) > e.offsetTop){
        e.classList.add("animate");
        } else {
        e.classList.remove("animate");
        }
    });
}
animationScroll();
window.addEventListener("scroll", function(){
    animationScroll();
});