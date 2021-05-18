/*class MemoGame {
    constructor(totalTime, cards) {
        this.cardsArray = cards;
        this.totalTime = totalTime;
        this.timeRemaining = totalTime;
        this.timer = document.getElementById('time-remaining')
        this.ticker = document.getElementById('flips');
    }

    startGame() {
        this.totalClicks = 0;
        this.timeRemaining = this.totalTime;
        this.cardToCheck = null;
        this.matchedCards = [];
        this.busy = true;
        setTimeout(() => {
            this.shuffleCards();
            this.countDown = this.startCountDown();
            this.busy = false;
        }, 700);
        this.hideCards();
        this.timer.innerText = this.timeRemaining;
        this.ticker.innerText = this.totalClicks; 
    }

    shuffleCards() { // Fisher-Yates Shuffle Algorithm.
        /*document.getElementById("test").innerHTML= this.cardsArray.length
        document.getElementById("test1").innerHTML= this.cardsArray[0]

        for (let i = this.cardsArray.length - 1; i > 0; i--) {
            let randIndex = Math.floor(Math.random() * (i + 1));
            this.cardsArray[randIndex].style.order = i;
            this.cardsArray[i].style.order = randIndex;
        }
        

    }

    startCountDown() {
        return setInterval(() => {
            this.timeRemaining--;
            this.timer.innerText = this.timeRemaining;
            if(this.timeRemaining === 0)
                this.gameOver();
        }, 1000);
    }

    flipCard(card) {
        if(this.canFlipCard(card)) {
            this.totalClicks++;
            this.ticker.innerText = this.totalClicks;
            card.classList.add('visible');

            if(this.cardToCheck) {
                this.checkForCardMatch(card);
            } else {
                this.cardToCheck = card;
            }
        }
    }

    hideCards() {
        this.cardsArray.forEach(card => {
            card.classList.remove('visible');
            card.classList.remove('matched');
        });
    }
    
    checkForCardMatch(card) {
        if(this.getCardType(card) === this.getCardType(this.cardToCheck))
            this.cardMatch(card, this.cardToCheck);
        else 
            this.cardMismatch(card, this.cardToCheck);

        this.cardToCheck = null;
    }
    cardMatch(card1, card2) {
        this.matchedCards.push(card1);
        this.matchedCards.push(card2);
        /*card1.classList.add('matched');
        card2.classList.add('matched');
    
        if(this.matchedCards.length === this.cardsArray.length){
            if(this.cardsArray.length==30){
                document.getElelentByClassName("update")[0].text="submit and go to home page";
                document.getElementsByClassName("update")[0].href="/update/"+this.totalClicks;
            }
            this.gameOver();
            
    }}

    cardMismatch(card1, card2) {
        this.busy = true;
        setTimeout(() => {
            card1.classList.remove('visible');
            card2.classList.remove('visible');
            this.busy = false;
        }, 1000);
    }

    getCardType(card) {
        return card.getElementsByClassName('card-front-value')[0].src;
    }

    gameOver() {
        alert("You have made " + this.totalClicks + " flips\nGot " + this.matchedCards.length/2 + " pair(s) correct\nTime taken: "  + (this.totalTime - this.timeRemaining) +'s');
        clearInterval(this.countDown);
        this.hideCards();
        this.busy=true;
        return (this.totalClicks, this.totalTime - this.timeRemaining);
    }

    canFlipCard(card) {
        
        return (!this.busy && !this.matchedCards.includes(card) && card !== this.cardToCheck);
    }
}

function ready() {
    let cards = Array.from(document.getElementsByClassName('card'));
    let game = new MemoGame(300, cards);

    game.startGame();

    cards.forEach(card => {
        card.addEventListener('click', () => {
            game.flipCard(card);
        });
    });
}

if(document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ready);
} else {
    ready();
}
 */
/**
 * Javascript file contains all of the functions require for the game to work
 */

/**
 * Class MemoGame with contrucstor which takes totalTime and cards array as parameters
 * @param totalTime the time limit for the game
 * @param cards the card array which contains all of the cards in an array
 */
 class MemoGame {
    constructor(totalTime, cards) {
        this.cardsArray = cards;
        this.totalTime = totalTime;
        this.timeRemaining = totalTime;
        this.timer = document.getElementById('time-remaining')
        this.ticker = document.getElementById('flips');
    }

    /**
     * Function to initialise the game
     */
    startGame() {
        this.totalClicks = 0;
        this.timeRemaining = this.totalTime;
        this.cardToCheck = null;
        this.matchedCards = [];
        this.busy = true;

        /**
         * Function to give a short break before loading the game
         * make the transition between the game page to other page and vice versa smoothly
         */
        setTimeout(() => {
            this.countDown = this.startCountDown();
            this.busy = false;
        }, 700);

        /**
         * Display the back card face
         * Display original time remaing and number of flips
         */
        this.hideCards();
        this.timer.innerText = this.timeRemaining;
        this.ticker.innerText = this.totalClicks; 
    }

    /**
     * Function to return the time remaining and display on web page,
     * is called after every interval
     * also check if the game is over given the time remaining
     * @returns time remaining
     */
    startCountDown() {
        return setInterval(() => {
            this.timeRemaining--;
            this.timer.innerText = this.timeRemaining;
            if(this.timeRemaining === 0)
                this.gameOver();
        }, 1000);
    }

    /**
     * Function to give user the result after the game is over
     * containing time taken, number of flips, and number of pairs correct
     * @returns number of flips and time taken
     */
     gameOver() {
        alert("You have made " + this.totalClicks + " flips\nGot " + this.matchedCards.length/2 + " pair(s) correct\nTime taken: "  + (this.totalTime - this.timeRemaining) +'s');
        clearInterval(this.countDown);
        this.hideCards();
        this.busy=true;
        return (this.totalClicks, this.totalTime - this.timeRemaining);
    }

    /**
     * Function to display the back card face for every card
     * by remove the visible attribute of the front card
     */
     hideCards() {
        this.cardsArray.forEach(card => {
            card.classList.remove('visible');
        });
    }

    /**
     * Function to display the front card face
     * by making the front card face visible
     * increment clicks if the user click on a card that can be fliped
     * assign this card to a variable to check for match with the next card
     * @param card the card that is being clicked by the player
     */
    flipCard(card) {
        if(this.canFlipCard(card)) {
            this.totalClicks++;
            this.ticker.innerText = this.totalClicks;
            card.classList.add('visible');

            if(this.cardToCheck) {
                this.checkForCardMatch(card);
            } else {
                this.cardToCheck = card;
            }
        }
    }

    /**
     * Function to check if the current card can be fliped
     * @param card the current card
     * @returns true if can be flip, false otherwise
     */
     canFlipCard(card) {
        return (!this.busy && !this.matchedCards.includes(card) && card !== this.cardToCheck);
    }

    /**
     * Function to check if 2 cards are the same
     * by comparing the source path of the two images that are being checked
     * add matched cards to a matched card array
     * otherwise flip back the cards
     * @param {*} card 
     */
    checkForCardMatch(card) {
        if(this.getCardType(card) === this.getCardType(this.cardToCheck))
            this.cardMatch(card, this.cardToCheck);
        else 
            this.cardMismatch(card, this.cardToCheck);

        this.cardToCheck = null;
    }

    /**
     * Function to get the source path of the image that is assigned to the current card
     * @param card the current card
     * @returns the source path of the image
     */
    getCardType(card) {
        return card.getElementsByClassName('card-front-value')[0].src;
    }

    /**
     * Function to push the matched cards to an array
     * game is over if the array contain every card
     * @param card1 first matched card
     * @param card2 second matched card
     */
    cardMatch(card1, card2) {
        this.matchedCards.push(card1);
        this.matchedCards.push(card2);

        if(this.matchedCards.length === this.cardsArray.length)
            if(this.cardsArray.length==30){
                document.getElementsByClassName("update")[0].text="submit and go to home page";
                document.getElementsByClassName("update")[0].href="/update/"+this.totalClicks;
            }
        this.gameOver();
    }

    /**
     * Function to flip back the cards if they are not the matched
     * block the ability to flip the card during this process
     * 
     * @param card1 the first card
     * @param card2 the second card
     */
    cardMismatch(card1, card2) {
        this.busy = true;
        setTimeout(() => {
            card1.classList.remove('visible');
            card2.classList.remove('visible');
            this.busy = false;
        }, 1000);
    }
}

/**
 * Function to be called when the this javascript file is loaded completely
 */
function ready() {
    let cards = Array.from(document.getElementsByClassName('card'));
    let game = new MemoGame(100, cards);

    game.startGame();

    /**
     * for each card, addEventListener of type click
     * for each click, pass the cards to flipCard function
     */
    cards.forEach(card => {
        card.addEventListener('click', () => {
            game.flipCard(card);
        });
    });
}

/**
 * If the page is not loaded yet,
 * wait for the page to load before run the code
 */
if(document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ready());
} else {
    ready();
}
