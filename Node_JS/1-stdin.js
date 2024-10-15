// I just realized on my last program I used a shebang for python,
// even though this is a javacsript program. Repition...

// When the program first runs, we want to display a message.
// ALso, since this is manual review, I'm replacing Holberton with Atlas.
console.log("Welcome to Atlas School, what is your name?");

// Now we get user input
process.stdin.on('data', (input) => {
    const UserName = input.toString().trim();
    console.log(`Your name is: ${UserName}`);

    process.stdin.pause();
});

// When process is over, show a message
process.stdin.on('pause', () => {
    console.log('This important software is now closing');
  });
