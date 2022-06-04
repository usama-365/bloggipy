/**
 * @file Contains the Javascript necessary for the signup forms
 * @author https://www.github.com/usama-365
 */

/**
 * Takes email address (in string) as input and returns the username part of
 * the email
 * @param {*} email Email address as string
 * @returns Part before the '@' in the email address if '@' is in the email, else the email address
 */
function generateEmailFromUsername(email) {
    /**
     * Takes an email address as input
     * Returns all the text as string before the '@' in email
     * Returns back the email if '@' is not in the email
     */
    if (typeof email === 'string' && email.includes('@'))
        return email.split('@')[0];
    else
        return email;
}

/**
 * If the document is ready, attach the event listeners to fill the username field by the email address
 */
document.addEventListener('DOMContentLoaded', function () {
    let emailInput = document.getElementById('email');
    document.onkeyup = function () {
        document.getElementById('username').value = generateEmailFromUsername(emailInput.value);
    }
});