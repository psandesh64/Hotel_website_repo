function showCategory(category) {
  // Hide all category items
  var categoryItems = document.getElementsByClassName('category-items');
  for (var i = 0; i < categoryItems.length; i++) {
    categoryItems[i].style.display = 'none';
  }

  // Show the selected category
  var selectedCategoryItems = document.getElementById(category + 'Items');
  if (selectedCategoryItems) {
    selectedCategoryItems.style.display = 'block';
  }
}
  // Show the first category items by default
var categoryItems = document.getElementsByClassName('category-items');
if (categoryItems.length > 0) {
  categoryItems[0].style.display = 'block';
}

// Slider for testimonials
const slides = document.querySelectorAll(".slide")
var counter = 0;
const totalSlides = slides.length; // Get the total number of slides
slides.forEach(
    (slide, index) => {
        slide.style.left = `${index*100}%`
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
        (slide) => {
            slide.style.transform = `translateX(-${counter*100}%)`
        }
    )

}

function playVideo() {
  var container = document.querySelector(".video-container");
  var content = document.querySelector(".hcontent15");
  var button = document.querySelector(".hbutton7");
  var imgquote = document.querySelector(".quote-child");
  var shadow = document.querySelector(".shadow1")

  // Hide other elements
  container.style.display = "block";
  content.style.display = "none";
  button.style.display = "none";
  imgquote.style.display = "none";
  shadow.style.display = "none";

}

// Initialize and add the map
let map;

async function initMap() {
  // The location of Uluru
  const position = { lat: 27.67155, lng: 85.34574 };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("map"), {
    zoom: 20,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  // The marker, positioned at Uluru
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "Sipalaya Info Tech",
  });
}

initMap();

// Slider for sliderdiv0
const slides0 = document.querySelectorAll(".slide0")
var counter0 = 0;
const totalSlides0 = slides0.length; // Get the total number of slides
slides0.forEach(
    (slide0, index) => {
        slide0.style.left = `${index*100}%`
    }
)
const goPrev0 = () => {
    
    if (counter0 > 0) {
        counter0-- // set the condition for counter to stop at 0
    }
    slideImage0()
    console.log(totalSlides0)
}
const goNext0 = () => {
    if (counter0 < totalSlides0/3-2) {
        counter0++ // set the condition for counter to stop at total number of slides
    }
    slideImage0()
    console.log(totalSlides0)
}
const slideImage0 = () => {
    slides0.forEach(
        (slide0) => {
            slide0.style.transform = `translateX(-${counter0*115.5}%)`
        }
    )

}