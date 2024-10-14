# Binary Search:General Skills

Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses. Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools! You can download the challenge files here:
* [challenge.zip](Binary Search/challenge.zip)  
`ssh -p 57062 ctf-player@atlas.picoctf.net`
Using the password `84b12bae`. Accept the fingerprint with `yes`, and ls once connected to begin. Remember, in a shell, passwords are hidden!

# Solution

challenge.zipを解凍して、中を見てみるとguessing_game.shというファイルが含まれている。
```
$ unzip challenge.zip
```
guessing_game.shの中を確認する。
```
$ strings guessing_game.sh 
            #!/bin/bash
            # Generate a random number between 1 and 1000
            target=$(( (RANDOM % 1000) + 1 ))
            echo "Welcome to the Binary Search Game!"
            echo "I'm thinking of a number between 1 and 1000."
            # Trap signals to prevent exiting
            trap 'echo "Exiting is not allowed."' INT
            trap '' SIGQUIT
            trap '' SIGTSTP
            # Limit the player to 10 guesses
            MAX_GUESSES=10
            guess_count=0
            while (( guess_count < MAX_GUESSES )); do
                read -p "Enter your guess: " guess
                if ! [[ "$guess" =~ ^[0-9]+$ ]]; then
                    echo "Please enter a valid number."
                    continue
                fi
                (( guess_count++ ))
                if (( guess < target )); then
                    echo "Higher! Try again."
                elif (( guess > target )); then
                    echo "Lower! Try again."
                else
                    echo "Congratulations! You guessed the correct number: $target"
                    # Retrieve the flag from the metadata file
                    flag=$(cat /challenge/metadata.json | jq -r '.flag')
                    echo "Here's your flag: $flag"
                    exit 0  # Exit with success code
                fi
            done
            # Player has exceeded maximum guesses
            echo "Sorry, you've exceeded the maximum number of guesses."
            exit 1  # Exit with error code to close the connection
```
1～1000までのランダムな数字が1つ用意されて、2分木探索を手動で行うことで、一致する数字を探すとフラグが出てくるらしい。  
2分木探索の方法は、まず真ん中の数字(500)をとりあえず入力して、それよりも高いor低いを確認する。さらに、入力した数字(500)と用意された数字が含まれる範囲の基準となる数字(1 or 1000)との真ん中の数字を入力していく。これを繰り返す。例えば、500を入力してhigherと出力された場合は、用意された数字は500～1000までに含まれるので、次は500と1000の真ん中の数字750を入力する。  
実行する。
```
$ ssh -p 57062 ctf-player@atlas.picoctf.net
ctf-player@atlas.picoctf.net's password: 
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500
Lower! Try again.
Enter your guess: 250
Higher! Try again.
Enter your guess: 375
Higher! Try again.
Enter your guess: 437
Lower! Try again.
Enter your guess: 406
Lower! Try again.
Enter your guess: 390
Higher! Try again.
Enter your guess: 398
Lower! Try again.
Enter your guess: 394 
Congratulations! You guessed the correct number: 394
Here's your flag: picoCTF{g00d_gu355_2e90d29b}
Connection to atlas.picoctf.net closed.
```
flagが得られた。

`picoCTF{g00d_gu355_2e90d29b}`
