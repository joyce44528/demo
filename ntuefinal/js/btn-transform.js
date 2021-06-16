(function(){

    let toggleBtn = document.querySelector('#btn');
    let loginbtn = document.querySelector('#login-btn');
    let signUpbtn= document.querySelector('#signUp-btn');

    let loginForm = document.querySelector('#login');
    let registerForm = document.querySelector('#register');
    let popupContent = document.querySelector('.popup__content');

    function enterLogin(e) {
        e.preventDefault()
        
        loginForm.style.transform = 'translateX(50%)';
        registerForm.style.transform = 'translateX(100%)';
        toggleBtn.style.transform = 'translateX(0)';
        signUpbtn.style.color = '#3d526e';
        loginbtn.style.color = '#fff';
    }

    function enterRegister(e) {
        e.preventDefault();

        // popupContent.style.backgroundImage= `linear-gradient(to left,
        //     rgba(#EFEAEB, .8), rgba(#D3DCE6, .9))`;
        loginForm.style.transform = 'translateX(-100%)';
        registerForm.style.transform = 'translateX(-50%)';
        toggleBtn.style.transform = 'translateX(100%)';
        signUpbtn.style.color = '#fff';
        loginbtn.style.color = '#3d526e';
    }


    loginbtn.addEventListener('click', enterLogin);
    signUpbtn.addEventListener('click', enterRegister);
}());

