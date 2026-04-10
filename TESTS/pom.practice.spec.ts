import {test} from '@playwright/test';
import {LoggedInPage} from '../object-pages/LoggedInPage';
import {HomePage} from '../object-pages/HomePage';

const info = [
    {username: 'student',       password: 'Password123'},
    {username: 'incorrectuser', password: 'Password123'},
    {username: 'student',       password: 'incorrectPassword'}
]

test.describe('Exercise 1: Practice Test Automation', () => {
    let loggedInPage: LoggedInPage, homePage: HomePage; 
    test.beforeEach(async({ page }) => {
        loggedInPage = new LoggedInPage(page);
        homePage = new HomePage(page);
        await loggedInPage.goto()
    });

    test('Test Case 1: Positive Login Test', async ({ }) => {
        await loggedInPage.login(info[0].username, info[0].password)
        await loggedInPage.verify_URL()
        await homePage.expected_text()
    });

    test('Test Case 2: Negative Username Test', async ({ }) => {
        await loggedInPage.login(info[1].username, info[1].password)
        await homePage.verify_message_invalid()
    });

    test('Test Case 3: Negative Password Test', async ({ }) => {
        await loggedInPage.login(info[2].username, info[2].password)
        await homePage.verify_message_invalid()
    });
});