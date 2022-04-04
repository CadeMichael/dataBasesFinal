/**
  * this file handles instantiating a new profile for a user of 
  * our application, plenty of fish in the s(ea)ql and add them 
  * to the database
  */ 

import inquirer from 'inquirer';

// question format
//  {
//    type: ,
//    name: ,
//    message: ,
//  }

// dealing with the "answers"
// you make a variable answers and access a specific answer with 
// the name you give it in the question variable
// ex: answers['name'] returns the answer given for name
const questions = [
  {
    type: "input",
    name: 'name',
    message: "what is your name ->",
  }
];

inquirer.prompt(questions).then((answers) => {
  console.log(answers['name']);
});
