burger = document.querySelector('.burger')
navbar = document.querySelector('.nav-bar5')
linksa = document.querySelector('.links17')
buttona = document.querySelector('.buttons6')
mybox = document.querySelector('.mybox')
heading2 = document.querySelector('.heading2')

burger.addEventListener('click',  ()=>{
  navbar.classList.toggle('hnav');
  linksa.classList.toggle('vclass');
  buttona.classList.toggle('vclass');
  mybox.classList.toggle('ttp');
  heading2.classList.toggle('ttpp');
})