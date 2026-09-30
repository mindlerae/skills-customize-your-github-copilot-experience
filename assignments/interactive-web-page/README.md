# 📘 Assignment: Interactive Web Page

## 🎯 Objective

Build a small interactive web page using HTML, CSS, and JavaScript. Practice selecting elements, responding to user events, and updating page content through the DOM.

## 📝 Tasks

### 🛠️ Build the Page Structure

#### Description
Complete the HTML structure for a personal greeting page. The page should include a heading, a text input for the visitor's name, a button, and an empty message area.

#### Requirements
Completed program should:

- Include a heading that identifies the page.
- Include an input with the id `name-input`.
- Include a button with the id `greet-button`.
- Include an empty paragraph with the id `greeting-message` for the JavaScript output.

### 🛠️ Respond to a Button Click

#### Description
Use JavaScript to listen for a click on the greet button and update the message area with a personalized greeting.

#### Requirements
Completed program should:

- Read the value entered in `name-input` when the button is clicked.
- Display `Hello, [name]! Welcome to my page.` in `greeting-message`.
- Display a helpful message when the input is empty instead of displaying a blank name.
- Keep the page in the browser instead of reloading it after the interaction.

### 🛠️ Add an Interactive Theme Choice

#### Description
Add a second button that changes the page between two visual themes. Use a CSS class and JavaScript instead of changing many individual styles from the script.

#### Requirements
Completed program should:

- Add a button with the id `theme-button`.
- Define a second theme using a CSS class such as `.dark-theme`.
- Toggle the theme class when the theme button is clicked.
- Update the button text so the available action is clear after each click.
