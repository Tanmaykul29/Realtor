const dynamicText = document.querySelector("h1 span");

const words = ["Real Estate Platform", "Property Listing Website", "Map for Real Estate Data", "Real Estate Information Hub"];

let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;

const typeEffect = () => {
    const currentWord = words[wordIndex];
    const currentChar = currentWord.substring(0, charIndex);
    // console.log(currentWord, currentChar);
    dynamicText.textContent = currentChar;
    dynamicText.classList.add("stop-blinking");

    if(!isDeleting && charIndex < currentWord.length){
        charIndex++;
        // 200 ms delay
        setTimeout(typeEffect, 200);
    }
    else if(isDeleting && charIndex > 0){
        charIndex--;
        setTimeout(typeEffect, 100);
    }
    else{
        isDeleting = !isDeleting;
        dynamicText.classList.remove("stop-blinking");
        wordIndex = !isDeleting ? (wordIndex+1)%words.length : wordIndex;
        setTimeout(typeEffect, 1200);
    }

}

typeEffect();