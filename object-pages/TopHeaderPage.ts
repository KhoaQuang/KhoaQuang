import {Page, expect} from '@playwright/test';

export class TopHeaderPage {
    readonly URL = 'http://zero.webappsecurity.com/bank/transfer-funds.html';
    constructor(private page:Page) {}
    get usernameButton() {
        return this.page.getByText('username');
    }

    get signInButton() {
        return this.page.getByText('Signin');
    }

    get logoutButton() {
        return this.page.getByRole('link', { name: 'Logout' });
    }

    async goto() {
        await this.page.goto(this.URL);
    }

    async verify_loggedOut() {
        await this.usernameButton.click()
        await this.logoutButton.click()
        await expect(this.signInButton).toBeVisible()
        console.log('The account is actually logged out')
    }
}