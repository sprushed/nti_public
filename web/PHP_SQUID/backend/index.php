<?php

echo("<title>PHP SQUID</title>");
echo "<h1>Pass all 6 games to win your reward!</> <br>";

error_reporting(E_ERROR | E_PARSE);


highlight_file(__FILE__);



function firstGame(){
  if (isset($_GET['game1_green']) and isset($_GET['game1_red'])){
      if ($_GET['game1_green'] == $_GET['game1_red'])
        echo "Not so easy!";
      else if (sha1($_GET['game1_green']) === sha1($_GET['game1_red'])){
        echo "Good job! You've past the first game! <br>";
        return;
      }
  }
  die();
}

function secondGame(){
  if (isset($_GET['game2'])){
      $honey = preg_replace("/honeycomb/", "", $_GET['game2']);
      if ($honey === "honeycomb"){
        echo "Excellent honeycomb! You can continue! <br>";
        return;
      } else {
        echo "Too bad figure for you...";
      }
  }
  die();
}

function fifthGame(){
    // My squid knows da way
    // So i will keep pass for map this way: "SquidX"
    // I know what my squid's name, so I can replace X and get the pass
    // For my demention: is is very popular US male name
    if (isset($_GET['game5'])){
        if (hash("md5", $_GET['game5']) === "97c581954095cfff4fe2421ec238dce7"){
          echo "You are familiar with my squid!<br>";
          return;
        } else {
          echo "This was unlucky...";
        }
    }
    die();

}

function squidGame(){
  if (isset($_GET['squidGame'])){
      if (hash("md5", $_GET['squidGame']) == "0"){
        echo "Unbelievable! <br>";
        return;
      } else {
        echo "So close...";
      }
  }
  die();
}

firstGame();
secondGame();
//No party allowed :(
//thirdGame();
//fourthGame();
fifthGame();

squidGame();

echo "You are the BEST PHP squid!<br>";
highlight_file("flag_for_winner.txt");

?>
