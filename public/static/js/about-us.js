function playVideo() {
    var container = document.querySelector(".video-container");
    var content = document.querySelector(".content15");
    var button = document.querySelector(".button7");
    var imgquote = document.querySelector(".quote-child");
    var shadow = document.querySelector(".shadow1")
  
    // Hide other elements
    container.style.display = "block";
    content.style.display = "none";
    button.style.display = "none";
    imgquote.style.display = "none";
    shadow.style.display = "none";
  
  }
  // Slider for quote
const slides = document.querySelectorAll(".slide1")
var counter = 0;
const totalSlides = slides.length; // Get the total number of slides
slides.forEach(
    (slide1, index) => {
        slide1.style.left = `${index*100}%`
    }
)
const goPrev = () => {
    
    if (counter > 0) {
        counter-- // set the condition for counter to stop at 0
    }
    slideImage()
}
const goNext = () => {
    if (counter < totalSlides - 1) {
        counter++ // set the condition for counter to stop at total number of slides
    }
    slideImage()
}
const slideImage = () => {
    slides.forEach(
        (slide1) => {
            slide1.style.transform = `translateX(-${counter*100}%)`
        }
    )

}
  // Slider for chef
  const slides2 = document.querySelectorAll(".slide2")
  var counter2 = 0;
  const totalSlides2 = slides2.length; // Get the total number of slides
  slides2.forEach(
      (slide2, index) => {
          slide2.style.left = `${index*100}%`
      }
  )
  const goPrev2 = () => {
      
      if (counter2 > 0) {
          counter2-- // set the condition for counter to stop at 0
      }
      slideImage2()
      updateSlideCounter()
  }
  const goNext2 = () => {
      if (counter2 < totalSlides2 - 3) {
          counter2++ // set the condition for counter to stop at total number of slides
      }
      slideImage2()
      updateSlideCounter()
  }
  const slideImage2 = () => {
      slides2.forEach(
          (slide2) => {
              slide2.style.transform = `translateX(-${counter2*106.7}%)`
          }
      )
  
  }
  const updateSlideCounter = () => {
    const slideCounter = document.querySelector(".div1");
    slideCounter.textContent = `${formatCounterValue(counter2 + 1)}`; // Update the counter value
  }
  
  const formatCounterValue = (value) => {
    return value < 10 ? `0${value}` : value; // Format the counter value to have leading zero if less than 10
  }