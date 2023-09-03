const checkbox_WHATSAPP = document.getElementById("checkbox-whatsapp");
const checkbox_EMAIL = document.getElementById("checkbox-email");
const block_inputs_WHATSAPP = document.getElementById("block-inputs-WHATSAPP");
const block_inputs_EMAIL = document.getElementById("block-inputs-EMAIL");
// ****
const checkbox_CPF = document.getElementById("checkbox-CPF");
const checkbox_CNPJ = document.getElementById("checkbox-CNPJ");
const block_inputs_CPF = document.getElementById("block-inputs-CPF");
const block_inputs_CNPJ = document.getElementById("block-inputs-CNPJ");

// ****** DOC_USER ******
checkbox_CPF.addEventListener("click", function(e) {
    checkbox_CNPJ.dataset.checkInput = "0";
    if (checkbox_CPF.dataset.checkInput === "0"){
        checkbox_CPF.dataset.checkInput = "1";
        checkbox_CPF.classList.toggle("active");
        checkbox_CNPJ.classList.toggle("active");
        
        block_inputs_CPF.style.display = "block";
        block_inputs_CNPJ.style.display = "none"
        document.getElementById("cnpj").value = "";
    } else {
        checkbox_CPF.dataset.checkInput = "1";
    }
});
checkbox_CNPJ.addEventListener("click", function(e) {
    checkbox_CPF.dataset.checkInput = "0";
    if (checkbox_CNPJ.dataset.checkInput === "0"){
        checkbox_CNPJ.dataset.checkInput = "1";
        checkbox_CNPJ.classList.toggle("active");
        checkbox_CPF.classList.toggle("active");
    
        block_inputs_CPF.style.display = "none";
        block_inputs_CNPJ.style.display = "block";
        document.getElementById("cpf").value = "";
    } else {
        checkbox_CNPJ.dataset.checkInput = "1";
    }
});

// ****** CONTACT_USER ******
checkbox_WHATSAPP.addEventListener("click", function(e) {
    checkbox_EMAIL.dataset.checkInput = "0";
    if (checkbox_WHATSAPP.dataset.checkInput === "0"){
        checkbox_WHATSAPP.dataset.checkInput = "1";
        checkbox_WHATSAPP.classList.toggle("active");
        checkbox_EMAIL.classList.toggle("active");
        
        block_inputs_WHATSAPP.style.display = "block";
        block_inputs_EMAIL.style.display = "none"
        document.getElementById("email").value = "";
    } else {
        checkbox_WHATSAPP.dataset.checkInput = "1";
    }
});
checkbox_EMAIL.addEventListener("click", function(e) {
    checkbox_WHATSAPP.dataset.checkInput = "0";
    if (checkbox_EMAIL.dataset.checkInput === "0"){
        checkbox_EMAIL.dataset.checkInput = "1";
        checkbox_EMAIL.classList.toggle("active");
        checkbox_WHATSAPP.classList.toggle("active");
        
        block_inputs_WHATSAPP.style.display = "none";
        block_inputs_EMAIL.style.display = "block"
        document.getElementById("whatsapp").value = "";
    } else {
        checkbox_EMAIL.dataset.checkInput = "1";
    }
});


// ****** TOGGLE_MODAL_CONTACT ******
function toggleModal(){
    let aux_eixo_y = 0;
    let eixo_y = window.pageYOffset;
    let tam_body_x = window.screen.width;
    let tam_body_y = window.screen.height;

    if (tam_body_x <= 560){
        aux_eixo_y = 255;
    }
    else if (tam_body_x >= 560 && tam_body_x < 740){
        aux_eixo_y = 245;
    }
    else if (tam_body_x >= 740){
        aux_eixo_y = 40;
    }
    let position_y = eixo_y + aux_eixo_y;
    document.querySelector(".modal-services-contact").classList.toggle("active");
    document.querySelector(".modal-services-contact.active").style.top = `${position_y}px`;
    document.querySelector("body").classList.toggle("acitve-modal");
    document.body.style.overflow = 'hidden';
}

if(document.querySelector(".invalid-inputs")){
    toggleModal();
}
function openModalServiceContatc(element){
    let data_service = element.dataset.service;
    let modal_form_select = document.getElementById("options-modal-contact-1");
    for (let i =0 ; i < modal_form_select.length; i++){
        if(data_service == modal_form_select.options[i].value){
            modal_form_select.options[i].selected = true;
        } else {
            modal_form_select.options[i].selected = false;
        }
    }
    toggleModal();
}
const BTN_CLOSE_servicePipedriveModal = document.querySelector('[data-target="BTN_CLOSE_servicePipedriveModal"]');
BTN_CLOSE_servicePipedriveModal.addEventListener("click", function(){
    document.querySelector(".modal-services-contact").classList.toggle("active");
    document.querySelector("body").classList.toggle("acitve-modal");
    document.body.style.overflow = 'auto';
});

