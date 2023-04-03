<?php

function getUserChoice() {
    echo "Enter your choice (rock, paper, or scissors): ";
    $input = trim(fgets(STDIN));
    $input = strtolower($input);

    if ($input === 'rock' || $input === 'paper' || $input === 'scissors') {
        return $input;
    } else {
        echo "Invalid input. Please try again.\n";
        return getUserChoice();
    }
}

function getComputerChoice() {
    $choices = ['rock', 'paper', 'scissors'];
    $index = array_rand($choices);
    return $choices[$index];
}

function determineWinner($userChoice, $computerChoice) {
    if ($userChoice === $computerChoice) {
        return "It's a draw!";
    }

    $winningConditions = [
        'rock' => 'scissors',
        'paper' => 'rock',
        'scissors' => 'paper'
    ];

    if ($winningConditions[$userChoice] === $computerChoice) {
        return "You win!";
    } else {
        return "You lose!";
    }
}

$userChoice = getUserChoice();
$computerChoice = getComputerChoice();

echo "You chose {$userChoice}.\n";
echo "The computer chose {$computerChoice}.\n";

$result = determineWinner($userChoice, $computerChoice);
echo $result . "\n";

?>
