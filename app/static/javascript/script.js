/**
 * Class MemoGame with contrucstor which takes totalTime and cards array as parameters
 * @param cards the card array which contains all of the cards in an array
 */
 class MemoGame { 
    constructor(cards) {
        this.cardsArray = cards;
        this.timer = document.getElementById('time-count')
        this.ticker = document.getElementById('flips');
    }

    /**
     * Function to initialise the game
     */
    startGame() {
        this.totalClicks = 0;
        this.timeCount = 0;
        this.cardToCheck = null;
        this.matchedCards = [];
        this.busy = true;

        this.cardsArray.forEach(card => {
            card.classList.add('visible');
        });

        /**
         * Function to give player a short period of time to remember cards before starting to play
         * All of the cards are shown for 2s
         * then flipped back and time starts 
         */
        setTimeout(() => {
            this.busy = false;
            this.hideCards();
            this.countUp = this.startCountUp();
        }, 2000);

        this.timer.innerText = this.timeCount;
        this.ticker.innerText = this.totalClicks; 
    }

    /**
     * Function to return the time count and display on web page,
     * is called after every interval
     * also check if the game is over if reach the maximum flips
     * @returns time count
     */
    startCountUp() {
        return setInterval(() => {
            this.timeCount++;
            this.timer.innerText = this.timeCount;
            if(this.totalClicks === 50)
                this.gameOver();
        }, 1000);
    }

    /**
     * Function to give user the result after the game is over
     * containing time taken, number of flips, and number of pairs correct
     */
     gameOver() {
        alert("GAME OVER!!! --- You have reached the flips count limit :(\nYou have made " + this.totalClicks + " flips\nGot " + this.matchedCards.length/2 + " pair(s) correct\nTime taken: "  + this.timeCount +'s');
        clearInterval(this.countUp);
        this.hideCards();
        this.busy=true;
        document.getElementsByClassName("again")[0].text="Play Again";
        document.getElementsByClassName("update")[0].text="Submit and Back";
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
     * @param card 
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
     * Victory if the array contain every card
     * @param card1 first matched card
     * @param card2 second matched card
     */
    cardMatch(card1, card2) {
        this.matchedCards.push(card1);
        this.matchedCards.push(card2);

        if(this.matchedCards.length === this.cardsArray.length) {
            if(this.matchedCards.length==10) {
                document.getElementsByClassName("update")[0].href="/update/"+this.totalClicks;
            }
            this.victory();
        }
    }

    /**
     * Function to give user the result after finishing the game
     * containing time taken, number of flips, and number of pairs correct
     * Display link to play again, submit and back or go to next round in assessment
     * 
     */
     victory() {
        alert("VICTORY!!! --- Well done :)\nYou have made " + this.totalClicks + " flips\nGot " + this.matchedCards.length/2 + " pair(s) correct\nTime taken: "  + this.timeCount +'s');
        clearInterval(this.countUp);
        this.hideCards();
        this.busy=true;
        document.getElementsByClassName("next")[0].text="Next";
        document.getElementsByClassName("again")[0].text="Play Again";
        document.getElementsByClassName("update")[0].text="Submit and Back";
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
    let game = new MemoGame(cards);

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