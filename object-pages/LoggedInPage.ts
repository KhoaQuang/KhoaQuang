import {expect, Page} from '@playwright/test';

export class LoggedInPage {
    readonly URL = 'https://practicetestautomation.com/practice-test-login/';
    constructor(private page:Page) {}
    get usernameInput() {
        return this.page.getByRole('textbox', { name: 'Username' });
    }

    get passwordInput() {
        return this.page.getByRole('textbox', { name: 'Password' });
    }

    get submitButton() {
        return this.page.getByRole('button', { name: 'Submit' });
    }
    
    async goto() {
        await this.page.goto(this.URL);
    }

    async login(username:string , password:string) {
        await this.usernameInput.fill(username);
        await this.passwordInput.fill(password);
        await this.submitButton.click();
    }

    async verify_URL() {
        await expect(this.page).toHaveURL(/logged-in-successfully/)
    }
}