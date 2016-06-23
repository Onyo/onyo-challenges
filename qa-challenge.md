# Onyo QA Challenge #

The main goal of the challenge is to analyse an Application Scenario, and define Test Cases that:
* Ensures the best user experience
* Map both the Happy Path (Basic Flow) and most common Alternate Flows.
* Take into account the key principles of the choosen platform (Mobile, Front-end or Backend)
* Take into account Accessibility concerns, when applicable

## Problem Description ##

The Use Case to be tested is a Login screen.
It has the following structure:
* Email Field
* Passowrd Field
* Button to reveal or hide the password (mobile only)
* Button to go to Reset Password screen
* Button to login

The fields should respect the following business rules:
* E-mail should not be empty
* E-mail should be at most 150 characters long
* E-mail should have a valid format
* Password should have at least 4 characters
* The e-mail should be already invited to use Onyo platform

You should worry about:
* Which kind of tests are most relevant for the choosen platform (Black box testing, white box testing, etc)
* Create a structure and describe the test so anyone without previous knowledge could execute them again
* Make the test cases automatable, when applicable

The Login Screen in each platform:
* Mobile
 * [iOS Application on App Store](https://itunes.apple.com/br/app/baked-potato/id1075878829?mt=8)
 * [Android Application on App Store](https://play.google.com/store/apps/details?id=com.onyo.bakedpotato)
* FrontEnd
 * [Front-End login screen](http://power.testing.onyo.com/#/login)
* Backend
 * API URL: https://api.testing.onyo.com/v1/mobile/user/login
 * Method: POST
 * Headers: Content-Type: application/json
 * Body example: { "email": "user@onyo.com", "password": "pass" }

## What you should deliver ##

* From 10 to 20 test cases, formatted in text and sent by e-mail.
* At least 3 test cases automated, using the tool of your choice
 * If possible, the resulting code should be sent by e-mail along with the Test Cases
 * Otherwise, it should be presented on the Technical Challenge review talk
