// JavaScript source code
        var player1 = "Player 1";

       

        // Function to change the player name
        function editNames() {
            player1 = prompt("Change Player1 name");
}

        function setName() {
            player1 = prompt("Choose your name");
}

        // Function to roll the dice
        function rollTheDice() {
            setTimeout(function () {
                var randomNumber1 = Math.floor(Math.random() * 20) + 1;
                
                document.querySelector(".img1").setAttribute("src", "img/D" + randomNumber1 + ".png");

                if (randomNumber1 >=2 && randomNumber1 <=19) {
                    document.querySelector("h1").innerHTML = player1 + " rolled:";
                }

                else if (randomNumber1 == 1) {
                    document.querySelector("h1").innerHTML = "You Lose, lol";
                }


                else if (randomNumber1 == 20) {
                    document.querySelector("h1").innerHTML = player1 + " WINS!";
                }

                else if (randomNumber1 >= 20) {
                    document.querySelector("h1").innerHTML = "yOU ABsOLuTE LOSeR";
                }
                    
            } ,25);
        }